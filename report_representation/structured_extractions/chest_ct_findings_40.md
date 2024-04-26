# Report text

```text
Devices/tubes/LINES: None.
Lungs/AIRWAYS: 
Left upper lobe superior division segmentectomy.
Few new pulmonary nodules, FOR EXAMPLE:
*  right upper lobe 5 mm (203:162)
*  left lower lobe 4 mm (203:360)
*  left lower lobe 4 mm (203:322).
Left lower lobe subsegmental atelectasis.
Upper lobe predominant centrilobular emphysema. Similar mild biapical pleural-parenchymal scarring. Similar reticulation, bronchiectasis and volume loss at the right upper lobe. The nonresected central airways are patent. Mild bronchial wall thickening.
PLEURA: No pleural effusions or pneumothoraces.
MEDIASTINUM: Small hiatal hernia. No suspicious thyroid nodules. Nonenlarged cardiac chambers. No pericardial effusion. No central pulmonary embolism. Severe coronary artery calcifications.
LYMPH NODES: Unchanged noncalcified and calcified mediastinal and hilar lymph nodes, including a partially calcified 12 mm retrotracheal lymph node (203:93), likely granulomatous. 
UPPER ABDOMEN: Reported separately.
CHEST WALL: No chest wall masses.
BONES: No suspicious lytic or blastic lesions. Postsurgical left 5th rib defect.
```

## Extracted findings

- [lobectomy](../../definitions/hood/lobectomy.json)
  - location: left upper lobe \[RID1303\]
- [nodule](../../definitions/hood/pulmonary-nodule.json)
  - location: right upper lobe \[RID1303\]
  - size:  5 mm
  - series image: 203:162
- [nodule](../../definitions/hood/pulmonary-nodule.json)
  - location: left lower lobe \[RID1338\]
  - size: 4 mm
  - series image: 203:360
- [nodule](../../definitions/hood/pulmonary-nodule.json)
  - location: left lower lobe \[RID1338\]
  - size: 4 mm
  - series image: 203:322
- atelectasis
  - location: left lower lobe \[RID1338\]
- [emphysema](../../definitions/hood/emphysema.json)
  - location: upper lobe \[RID1303\], \[RID1303\]
  - type: centrilobular
- [scarring](../../definitions/nuance/apical_pulmonary_scarring.json)
  - severity: mild
  - location: biapical \[RID28584\]
- [bronchiectasis](../../definitions/hood/bronchiectasis.json)
  - presence: present
- volume loss
  - location: right upper lobe \[RID1303\]
- [bronchial wall thickening](../../definitions/hood/bronchial-wall-thickening.md)
  - severity: mild
- [pleural effusion](../../definitions/hood/pleural-effusion.json)  
  - severity: moderate to large
- [pneumothorax](../../definitions/hood/pneumothorax.md)
  - presence: absent
- [hiatal hernia](../../definitions/hood/hiatal-hernia.json)
  - sevetity: small
- [thyroid nodule](../../definitions/hood/thyroid-nodule.md)
  - presence: absent
- [cardiac chamber enlargement](../../definitions/upmedic/Cardiomegaly.cde.md)
  - present: absent
- [pericardial effusion](../../definitions/hood/pericardial-effusion.md)
  - presence: absent
- [central pulmonary embolism](../../definitions/hood/pulmonary-emboli.json) \[RID974\]
  - presence: absent
- [vessel calcification](../../definitions/nuance/coronary_artery_calcification.json)
  - location: coronary artery [RID486\], \[RID544\]
  - severity: severe
- [calcified granuloma](../../definitions/hood/calcified-granuloma.md)
  - size: 12 mm
  - series image: 203:93
  - location: retrotracheal lymph node
- [lytic bony lesions](../../definitions/hood/lytic-lesion.md)
  - presence: absent
- [blastic bony lesion](../../definitions/hood/sclerotic-lesion.md)
  - presence: absent
- [rib defect](../../definitions/hood/healed-rib-fracture.json)
  - location: left fifth rib \[RID28591_RID6155_RID5824\]
- [chest wall mass](../../definitions/hood/chest-wall.json)  
  - presence: absent
  
## Composite Negative Statements

- Lungs
  - The nonresected central airways are patent.
- Pleura
  - No pleural effusions or pneumothoraces.
- Mediastinum
  - Devices/tubes/LINES: None.
  - No suspicious thyroid nodules. Nonenlarged cardiac chambers. No pericardial effusion. No central pulmonary embolism.
  - Unchanged noncalcified and calcified mediastinal and hilar lymph nodes.
  - No chest wall masses.
- Bones
  - No suspicious lytic or blastic lesions.
