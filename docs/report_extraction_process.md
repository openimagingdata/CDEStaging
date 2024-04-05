# Manual Report Extraction

The goal is to look at radiology report language:

> Pulmonary Angiogram:
> 
> The pulmonary arteries are well opacified. There is no pulmonary embolus.
>
> Devices/Tubes/Lines: None.
>
> Lungs: Consolidative opacity in the right lower lobe. Linear atelectasis in the right upper lobe.
> Mild groundglass changes in the right lower lobe (4:195) overlying the pleural effusion, likely
> representing early atelectasis.
>
> No consolidation in the left lung.
>
> Pleura: Moderate pleural effusion in the right tracking to the apex. No surrounding enhancement.
> No left pleural effusion. No pneumothorax.
>
> Mediastinum: Mild leftward mediastinal shift. No thyroid nodules. The heart is within normal limits.
> Trace pericardial effusion.
>
> Lymph Nodes: No enlarged supraclavicular, axillary, mediastinal, or hilar lymph nodes.
>
> Upper Abdomen: Contrast in the left upper quadrant bowel loops likely due to CT abdomen pelvis
> performed ---. Status post gastroduodenal artery embolization
>

..into a list of mini-observations:

```md
- pulmonmary embolism
  - presence: absent
- pulmonary consolidation
  - presence: present
  - location: right lower lobe
- atelectasis
  - presence: present
  - type: linear
  - location: right upper lobe
- groundglass opacity
  - presence: present
  - location: right lower lobe
  - series image: 4:195
- pulmonary consolidation:
  - presence: absent
  - location: left lung
- pleural effusion
  - presence: present
  - side: right
- pleural effusion
  - presence: absent
  - side: left
- pneumothorax
  - presence: absent
```
...and so on.

Other issues:
- Need to make sure we have the finding, attribute, and value names correspond to those in our finding defintions
- Should look for blanket negative statements like "Lungs are clear", "Heart and pericardium are normal" and
 list them in a separate file for us to catalog ang look at.
