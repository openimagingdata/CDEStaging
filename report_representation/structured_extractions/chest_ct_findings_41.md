# Report text

```text
Devices/Tubes/LINES: None.
LUNGS: Status post bilateral lung transplantation. No evidence of bronchial stenosis.
There are multiple irregular nodules in a peribronchial distribution which have decreased in size since 12/18/2023. For example a 10 mm right middle lobe nodule, 5:36, previously measured 23 mm. A 9 mm right lower lobe nodule, 5:243, previously measured 15 mm.
Unchanged linear atelectasis right lower lung. No air trapping. No change on prone imaging.
PLEURA: Decrease in small right pleural effusion. 
MEDIASTINUM: Normal. No thyroid nodules. Heart and pericardium are normal. Mild amount of coronary calcifications.
LYMPH NODES: Normal. No enlarged supraclavicular, axillary, mediastinal, or hilar lymph nodes.
UPPER ABDOMEN: Normal. No abnormality detected in the visualized upper abdomen. Absence of intravenous contrast limits sensitivity for detecting solid organ findings.
CHEST WALL: Normal. No chest wall mass.
BONES: No suspicious lytic or blastic lesions. Status post clamshell sternotomy
```

## Extracted findings

- [nodule](../../definitions/hood/pulmonary-nodule.json)
  - size: 10 mm
  - location: right middle lobe \[RID1310\]
  - series image: 5:36
- [nodule](../../definitions/hood/pulmonary-nodule.json)
  - size: 9 mm
  - location: right lower lobe \[RID1315\]
  - series image: 5:243
- lung transplant
  - presence: present
- [bronchial stenosis](../../definitions/hood/bronchial-stenosis.md)
  - presence: absent
- [airtrapping](../../definitions/upmedic/AirTrapping.cde.md)
  - presence: absent
- atelectasis
  - location: right lower lung \[RID1315\]
- [pleural effusion](../../definitions/hood/pleural-effusion.json)  
  - location: righ side
  - volume: small
- [vessel calcification](../../definitions/nuance/coronary_artery_calcification.json)
  - location: coronary artery [RID486\], \[RID544\]
  - severity: mild
- [thyroid nodule](../../definitions/hood/thyroid-nodule.md)
  - presence: absent
- [cardiomegaly](../../definitions/upmedic/Cardiomegaly.cde.md)
  - present: absent
- lymphadenopathy
  - presence: absent
- [chest wall mass](../../definitions/hood/chest-wall.json)  
  - presence: absent
- [lytic bony lesions](../../definitions/hood/lytic-lesion.md)
  - presence: absent
- [blastic bony lesion](../../definitions/hood/sclerotic-lesion.md)
  - presence: absent
- [sternotomy changes](../../definitions/hood/median-sternotomy.md)
  - presence: present

## Compositve Negative Statements

- Lungs
  - No evidence of bronchial stenosis.
Unchanged linear atelectasis right lower lung. No air trapping. No change on prone imaging.
- Mediastinum
  - Devices/Tubes/LINES: None.
  - Normal. No thyroid nodules. Heart and pericardium are normal.
  - No enlarged supraclavicular, axillary, mediastinal, or hilar lymph nodes.
- Abdomen
  - Normal. No abnormality detected in the visualized upper abdomen. Absence of intravenous contrast limits sensitivity for detecting solid organ findings.
  - Normal. No chest wall mass.
- Bones
  - No suspicious lytic or blastic lesions.
