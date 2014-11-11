import FWCore.ParameterSet.Config as cms

pfTrackElec = cms.EDProducer("PFElecTkProducer",
    TrajInEvents = cms.bool(False),
    Fitter = cms.string('GsfElectronFittingSmoother'),
    ModeMomentum = cms.bool(True),
    applyEGSelection = cms.bool(False),        
    applyGsfTrackCleaning = cms.bool(True),
    applyAlsoGsfAngularCleaning = cms.bool(True),
    maxDEtaGsfAngularCleaning = cms.double(0.05),
    maxDPhiBremTangGsfAngularCleaning = cms.double(0.05),                         
    useFifthStepForTrackerDrivenGsf = cms.bool(False),
    useFifthStepForEcalDrivenGsf = cms.bool(False),                         
    MaxConvBremRecoPT = cms.double(49.0),                         
    MinDEtaGsfSC = cms.double(0.06),
    MinDPhiGsfSC = cms.double(0.15),
    MinSCEnergy = cms.double(4.0),                         
    TTRHBuilder = cms.string('WithTrackAngle'),
    GsfTrackModuleLabel = cms.InputTag("electronGsfTracks"),
    Propagator = cms.string('fwdElectronPropagator'),
    PFRecTrackLabel = cms.InputTag("pfTrack"),
    PFEcalClusters  = cms.InputTag("particleFlowClusterECAL"),                 
    PrimaryVertexLabel = cms.InputTag("offlinePrimaryVertices"),                         
    useConvBremFinder  = cms.bool(True),
    pf_convBremFinderID_mvaCut =  cms.double(0.2),
    pf_convBremFinderID_mvaWeightFile = cms.string('RecoParticleFlow/PFTracking/data/MVAnalysis_BDT.weights_convBremFinder_19Apr_IntToFloat.txt'),   
    PFNuclear = cms.InputTag("pfDisplacedTrackerVertex"),
    PFConversions = cms.InputTag("pfConversions"),
    PFV0 = cms.InputTag("pfV0"),
    useNuclear = cms.bool(False),
    useV0 = cms.bool(False), 
    useConversions = cms.bool(False),
    debugGsfCleaning = cms.bool(False)                     
)



