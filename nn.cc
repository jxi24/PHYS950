void nn(Int_t nTrain=100) {
    // Multi-Layer Perceptron
    if(!gROOT -> GetClass("TMultiLayerPerceptron")) {
        gSystem -> Load("libMLP");
    }

    // Prepare inputs
    // The 2 trees are merged into one, and a "type" branch,
    // equal to 1 for the signal and 0 for the background is added
    const char *fsig = "sig_test.root";
    const char *fbkgd = "bkgd_test.root";
    TFile *sig = 0, *bkgd = 0;

    sig = TFile::Open(fsig);
    bkgd = TFile::Open(fbkgd);

    if(!sig || !bkgd) {
        std::cout << "Error: Input file doesn't exist!" << std::endl;
        exit(-1);
    }

    TTree *signal = (TTree *)sig->Get("physics");
    TTree *background = (TTree *)bkgd->Get("physics");
    TTree *simu = new TTree("MonteCarlo", "Filtered Monte Carlo Events");
    Double_t lead_pt, sub_pt, lead_eta, sub_eta, mee, pse;
    Int_t type;
    signal -> SetBranchAddress("lead_pt", &lead_pt);
    signal -> SetBranchAddress("sub_pt", &sub_pt);
    signal -> SetBranchAddress("lead_eta", &lead_eta);
    signal -> SetBranchAddress("sub_eta", &sub_eta);
    signal -> SetBranchAddress("mee", &mee);
    signal -> SetBranchAddress("pse", &pse);
    background -> SetBranchAddress("lead_pt", &lead_pt);
    background -> SetBranchAddress("sub_pt", &sub_pt);
    background -> SetBranchAddress("lead_eta", &lead_eta);
    background -> SetBranchAddress("sub_eta", &sub_eta);
    background -> SetBranchAddress("mee", &mee);
    background -> SetBranchAddress("pse", &pse);
    simu -> Branch("lead_pt", &lead_pt, "lead_pt/D");
    simu -> Branch("sub_pt", &sub_pt, "sub_pt/D");
    simu -> Branch("lead_eta", &lead_eta, "lead_eta/D");
    simu -> Branch("sub_eta", &sub_eta, "sub_eta/D");
    simu -> Branch("mee", &mee, "mee/D");
    simu -> Branch("pse", &pse, "pse/D");
    simu -> Branch("type", &type, "type/I");
    type = 1;
    for(Int_t i = 0; i < signal -> GetEntries(); i++) {
        signal -> GetEntry(i);
        simu -> Fill();
    }
    type = 0;
    for(Int_t i = 0; i < background -> GetEntries(); i++) {
        background -> GetEntry(i);
        simu -> Fill();
    }

    // Build and train the NN, sigma is used as the cross-section weight
    TMultiLayerPerceptron *mlp =
        new TMultiLayerPerceptron("@lead_pt,@sub_pt,@lead_eta,@sub_eta,@mee,@pse:5:3:type",
                "sigma",simu,"Entry$%2","(Entry$+1)%2");
    mlp -> Train(nTrain, "text, graph, update=10");
    mlp -> Export("test","C++");

    // Use TMLPAnalyzer to see what it looks for
    TCanvas* mlpa_canvas = new TCanvas("mlpa_canvas", "Network analysis");
    mlpa_canvas -> Divide(2,2);
    TMLPAnalyzer ana(mlp);

    // Initialization
    ana.GatherInformations();
    // Output to the console
    ana.CheckNetwork();
    mlpa_canvas -> cd(1);
    // Shows how each variable influences the network
    ana.DrawDInputs();
    mlpa_canvas -> cd(2);
    // Shows the network structure
    mlp -> Draw();
    mlpa_canvas -> cd(3);
    // Draws the resultsing network
    ana.DrawNetwork(0,"type==1","type==0");
    mlpa_canvas -> cd(4);
    // Use the NN to plot the results for each sample
    // This will give approx. the same results as DrawNetwork.
    // All entries are used, while DrawNetwork focuses on
    // the test sample. Also the xaxis range is manually set.
    TH1D *bg = new TH1D("bgh", "NN output", 50, -0.5, 1.5);
    TH1D *sign = new TH1D("sigh", "NN output", 50, -0.5, 1.5);
    bg -> SetDirectory(0);
    sig -> SetDirectory(0);
    Double_t params[6];
    for(Int_t i = 0; i < background -> GetEntries(); i++) {
        background -> GetEntry(i);
        params[0] = lead_pt;
        params[1] = sub_pt;
        params[2] = lead_eta;
        params[3] = sub_eta;
        params[4] = mee;
        params[5] = pse;
        bg -> Fill(mlp->Evaluate(0,params));
    }
    for(Int_t i = 0; i < signal -> GetEntries(); i++) {
        signal -> GetEntry(i);
        params[0] = lead_pt;
        params[1] = sub_pt;
        params[2] = lead_eta;
        params[3] = sub_eta;
        params[4] = mee;
        params[5] = pse;
        sign -> Fill(mlp->Evaluate(0,params));
    }
    bg -> SetLineColor(kBlue);
    bg -> SetFillStyle(3008);
    bg -> SetFillColor(kBlue);
    sign -> SetLineColor(kRed);
    sign -> SetFillStyle(3008);
    sign -> SetFillColor(kRed);
    bg -> SetStats(0);
    sign -> SetStats(0);
    bg -> Draw();
    sign -> Draw("same");
    TLegend *leg = new TLegend(0.75,0.80,0.95,0.95);
    leg -> AddEntry(bg, "Background");
    leg -> AddEntry(sign, "Signal");
    leg -> Draw("same");
    mlpa_canvas -> cd(0);
}
    


