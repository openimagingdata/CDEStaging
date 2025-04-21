# Artery

## Identification  

- **VesselName**  
  - DataType: string  
  - Description: Standard anatomical name of the artery  

- **Laterality**  
  - DataType: string  
  - Possible values: left, right, midline  
  - Description: Side of the body  

- **Segment**  
  - DataType: string  
  - Possible values: proximal, mid, distal, cervical, petrous, abdominal, thoracic  
  - Description: Anatomical segment of the artery  

---

## AnatomicVariation

- **VariantClassification**  
  - DataType: string  
  - Possible values: typical, accessory, aberrant  
  - Description: Classification of origin variation  

- **ReplacedOrigin**  
  - DataType: string  
  - Description: Name of artery from which this artery arises when origin is not typical  

---

## 3 DeviceAndProcedureFindings  

- **ProcedureTypes**  
  - DataType: array of strings  
  - Possible values: coil embolization, surgical ligation, stenting, bypass graft, endarterectomy, anastomosis  
  - Description: Any therapeutic intervention applied to the vessel  

- **DeviceStatus**  
  - DataType: string  
  - Possible values: patent, fractured, migrated, in stent restenosis, endoleak type one, endoleak type two, endoleak type three  
  - Description: Current status of any implanted device  

---

## 4 LuminalCaliber  

- **Diameter**  
  - DataType: number  
  - Units: millimeters  
  - Description: Maximal measured luminal diameter  

- **DilationPresent**  
  - DataType: boolean  
  - Description: Presence of vessel dilation beyond normal range  

- **AneurysmTypes**  
  - DataType: array of strings  
  - Possible values: fusiform aneurysm, saccular aneurysm, mycotic aneurysm, pseudoaneurysm  
  - Description: Morphologic classification of aneurysm  

- **StenosisSeverity**  
  - DataType: string  
  - Possible values: mild, moderate, severe, critical  
  - Description: Luminal narrowing percentage classification  
    - mild indicates one percent to forty nine percent narrowing  
    - moderate indicates fifty percent to sixty nine percent narrowing  
    - severe indicates seventy percent to ninety nine percent narrowing  
    - critical indicates complete narrowing  

- **OcclusionPresent**  
  - DataType: boolean  
  - Description: Complete vessel occlusion including pseudo‑occlusion  

---

## 5 WallIntegrityAndPathology  

- **DissectionFeatures**  
  - DataType: array of strings  
  - Possible values: intimal flap, true lumen, false lumen  
  - Description: Key features of arterial dissection  

- **IntramuralHematomaPresent**  
  - DataType: boolean  
  - Description: Blood within vessel wall  

- **TraumaticLacerationPresent**  
  - DataType: boolean  
  - Description: Vessel wall tear or transection  

- **WallCalcificationPresent**  
  - DataType: boolean  
  - Description: Calcified atherosclerotic plaque  

- **PlaqueUlcerationPresent**  
  - DataType: boolean  
  - Description: Ulceration of atherosclerotic plaque  

- **VasculitisFeaturesPresent**  
  - DataType: boolean  
  - Description: Vessel wall thickening with perivascular stranding  

---

## 6 IntraluminalContent  

- **ThrombusType**  
  - DataType: string  
  - Possible values: acute thrombus, chronic thrombus, mixed thrombus  
  - Description: Characterization of intraluminal thrombus  

- **EmbolusPresent**  
  - DataType: boolean  
  - Description: Intraluminal embolic material  

- **ForeignMaterialType**  
  - DataType: string  
  - Possible values: air, filter, graft, stent  
  - Description: Non‑thrombotic intraluminal content  

---

## 7 Hemodynamics  

- **ActiveBleedPresent**  
  - DataType: boolean  
  - Description: Contrast extravasation indicating active hemorrhage  

- **ArteriovenousFistulaPresent**  
  - DataType: boolean  
  - Description: Direct connection from artery to vein  

- **AVMComponentPresent**  
  - DataType: boolean  
  - Description: Artery forms part of an arteriovenous malformation  

- **DownstreamIschemiaPresent**  
  - DataType: boolean  
  - Description: Evidence of organ infarction or hypoperfusion downstream  

---

## 8 ContourAndCourse  

- **VesselContourType**  
  - DataType: string  
  - Possible values: normal contour, beaded, irregular, tortuous, kinked, looped  
  - Description: Morphology of vessel course  

- **CompressionSyndromeType**  
  - DataType: string  
  - Possible values: median arcuate ligament syndrome, nutcracker syndrome, May Thurner syndrome, superior mesenteric artery syndrome, thoracic outlet syndrome  
  - Description: Vascular compression syndrome involving this artery  

---

## 9 SecondarySigns  

- **CollateralFormationPresent**  
  - DataType: boolean  
  - Description: Development of collateral vessels  

- **EarlyVenousDrainagePresent**  
  - DataType: boolean  
  - Description: Early venous opacification indicating arteriovenous shunting  

- **PerivascularHematomaPresent**  
  - DataType: boolean  
  - Description: Blood collection adjacent to the vessel  

- **MassEffectPresent**  
  - DataType: boolean  
  - Description: Compression of adjacent structures by vascular abnormality  

---

## 10 DiagnosticCertainty  

- **CertaintyLevel**  
  - DataType: string  
  - Possible values: definite, probable, indeterminate  
  - Description: Reporter confidence in the finding  
