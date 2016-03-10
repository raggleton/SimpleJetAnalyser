"""
This config is for running with JEC in a GlobalTag.
This is to give a reference for each set of JEC.

74X_mcRun2_asymptotic_v5 :  Summer15_25nsV7
76X_mcRun2_asymptotic_RunIIFall15DR76_v1 : Fall15_25nsV2
"""

import FWCore.ParameterSet.Config as cms

process = cms.Process('RAW2DIGI')

process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat0to50NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/20000/1E2B5203-7AAA-E511-B6FD-0CC47A4D762A.root'),
)

from Configuration.AlCa.GlobalTag import GlobalTag
# process.GlobalTag = GlobalTag(process.GlobalTag, '74X_mcRun2_asymptotic_v5', '')  # Summer15_25nsV7
process.GlobalTag = GlobalTag(process.GlobalTag, '76X_mcRun2_asymptotic_RunIIFall15DR76_v1', '')  # Fall15_25nsV2 JEC

process.jetAnalysis = cms.EDAnalyzer('JetAnalyser')

process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string('L1Ntuple_summer15V7_GT.root')
    # fileName = cms.string('L1Ntuple_fall15V2_GT.root')
)

# Path and EndPath definitions
process.load('JetMETCorrections.Configuration.JetCorrectors_cff')

process.p = cms.Path(process.ak4PFCHSL1FastL2L3CorrectorChain + process.jetAnalysis)
