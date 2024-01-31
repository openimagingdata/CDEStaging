# Degenerative changes

## Shoulder girdle

// Individual instances can be logged. For example, if the report describes "moderate degenerative changes of the glenohumeral and acromioclavicular joints", then two instances of the following schema should be generated.

// Can include an option to swap out "osteoarthritis" for "degenerative changes."

- Joint
  - Acromioclavicular
  - Glenohumeral
  - Sternoclavicular
  - Sternomanubrial
  - Sternocostal
  - Costotransverse
- Laterality
  - Right
  - Left
  - Bilateral
- Severity
  - Mild
  - Moderate
  - Severe
    - Synonym: advanced, marked
- Effusion
  - Y / N
- Joint bodies
  - Y / N

## Spine

- Region <!--Lower cervical and upper lumbar spine may be within the field of view-->
  - Cervical spine
    - Descriptor: imaged, lower
  - Thoracic spine
  - Lumbar spine
    - Descriptor: imaged, upper
- Focality <!--This allows us to encompass focal observations of degenerative changes as well as more broad statements like "mild multilevel degenerative changes of the thoracic spine.-->
  - Diffuse
    - Synonym: multilevel
    - Severity
      - Mild
      - Moderate
      - Severe
        - Synonym: advanced, marked
  - Worst at: (multiselect)
    - C7-T1
    - T1-T2
    - T2-T3
    - T3-T4
    - T4-T5
    - T5-T6
    - T6-T7
    - T7-T8
    - T8-T9
    - T9-T10
    - T10-T11
    - T11-T12
    - T12-L1
- Spinal canal narrowing
  - Mild
  - Moderate
  - Severe
    - Synonym: advanced, marked
- Schmorl nodes
- Disc height loss <!--Severity of these findigns may either be reported as individual observations, or if a report says "moderate disc height loss and endplate degenerative changes," then severity would be logged as "moderate" for both findings.-->
  - Mild
  - Moderate
  - Severe
    - Synonym: advanced, marked
- Endplate sclerosis
  - Mild
  - Moderate
  - Severe
    - Synonym: advanced, marked
