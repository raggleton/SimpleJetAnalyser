"""
This config is for running with JEC in a SQL file.
Note that we purposely use the *wrong* GlobalTag to ensure it's actually using the SQL file!

GT:
74X_mcRun2_asymptotic_v5 :  Summer15_25nsV7
76X_mcRun2_asymptotic_RunIIFall15DR76_v1 : Fall15_25nsV2
"""
import FWCore.ParameterSet.Config as cms

process = cms.Process('JET')
process.load('Configuration.StandardSequences.Services_cff')
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
process.GlobalTag = GlobalTag(process.GlobalTag, '74X_mcRun2_asymptotic_v5', '')  # Summer15_25nsV7
# process.GlobalTag = GlobalTag(process.GlobalTag, '76X_mcRun2_asymptotic_RunIIFall15DR76_v1', '')  # Fall15_25nsV2 JEC

process.load("CondCore.DBCommon.CondDBCommon_cfi")
from CondCore.DBCommon.CondDBSetup_cfi import *
process.jec = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
        ),
    timetype = cms.string('runnumber'),
    toGet = cms.VPSet(
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            # tag    = cms.string('JetCorrectorParametersCollection_Summer15_25nsV7_MC_AK4PFchs'),
            tag    = cms.string('JetCorrectorParametersCollection_Fall15_25nsV2_MC_AK4PFchs'),
            label  = cms.untracked.string('AK4PFchs')  # !!! NOTE IT'S LOWER CASE chs NOT UPPERCASE. FAILURE TO DO THIS WILL RUIN YOUR LIFE. LITERALLY.
            ),
        ),
    # connect = cms.string('sqlite:Summer15_25nsV7_MC.db')
    connect = cms.string('sqlite:Fall15_25nsV2_MC.db')
)

## add an es_prefer statement to resolve a possible conflict from simultaneous connection to a global tag
process.es_prefer_jec = cms.ESPrefer('PoolDBESSource','jec')

process.jetAnalysis = cms.EDAnalyzer('JetAnalyser')

process.TFileService = cms.Service(
    "TFileService",
    # fileName = cms.string('L1Ntuple_summer15V7_200_wrongGT_db.root')
    fileName = cms.string('L1Ntuple_fall15V2_2_wrongGT_db.root')
)

# Path and EndPath definitions
process.load('JetMETCorrections.Configuration.JetCorrectors_cff')

process.p = cms.Path(process.ak4PFCHSL1FastL2L3CorrectorChain + process.jetAnalysis)
