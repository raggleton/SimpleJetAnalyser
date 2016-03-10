// -*- C++ -*-
//
// Package:    Demo/JetAnalyser
// Class:      JetAnalyser
// 
/**\class JetAnalyser JetAnalyser.cc Demo/JetAnalyser/plugins/JetAnalyser.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Robin Aggleton
//         Created:  Wed, 09 Mar 2016 20:37:57 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/ESHandle.h"

// cond formats
#include "JetMETCorrections/JetCorrector/interface/JetCorrector.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TTree.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class JetAnalyser : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit JetAnalyser(const edm::ParameterSet&);
      ~JetAnalyser();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------

      // output file
      edm::Service<TFileService> fs_;

      // tree
      TTree * tree_;

      // EDM input tags
      edm::EDGetTokenT<reco::PFJetCollection>     pfJetToken_;
      edm::EDGetTokenT<reco::JetCorrector>        jecToken_;

      float et_, etCorr_, corrFactor_;

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
JetAnalyser::JetAnalyser(const edm::ParameterSet& iConfig):
    et_(0.),
    etCorr_(0.),
    corrFactor_(0.)
{
   //now do what ever initialization is needed
   usesResource("TFileService");
   pfJetToken_ = consumes<reco::PFJetCollection>(iConfig.getUntrackedParameter("pfJetToken",edm::InputTag("ak4PFJetsCHS")));
   jecToken_ = consumes<reco::JetCorrector>(iConfig.getUntrackedParameter<edm::InputTag>("jecToken",edm::InputTag("ak4PFCHSL1FastL2L3Corrector")));
   tree_=fs_->make<TTree>("JetRecoTree", "JetRecoTree");
   tree_->Branch("et", &et_);
   tree_->Branch("etCorr", &etCorr_);
   tree_->Branch("corrFactor", &corrFactor_);
}


JetAnalyser::~JetAnalyser()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
JetAnalyser::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   edm::Handle<reco::PFJetCollection> pfJets;
   iEvent.getByToken(pfJetToken_, pfJets);
   // reco::PFJetCollection * jets = pfJets.product();

   edm::Handle<reco::JetCorrector> pfJetCorr;
   iEvent.getByToken(jecToken_, pfJetCorr);
   
   LogInfo("JetAnal") << "Njets: " << pfJets->size();
   reco::PFJetCollection::const_iterator itr = pfJets->begin();
   reco::PFJetCollection::const_iterator itrEnd = pfJets->end();
   int c = 0;
   for(; itr != itrEnd; ++itr) {
       corrFactor_ = pfJetCorr.product()->correction(*itr);
       std::cout << c << " ET PRE " << itr->et() << " ET POST " << corrFactor_ * itr->et() << " ETA " << itr->eta() << " PHI " << itr->phi() << std::endl;
       c++;
       et_ = itr->et();
       etCorr_ = itr->et() * corrFactor_; 
       tree_->Fill();
   }
}

// ------------ method called once each job just before starting event loop  ------------
void 
JetAnalyser::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
JetAnalyser::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
JetAnalyser::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetAnalyser);
