# Breast Density CDE Specification

## Overview

This document outlines the **Common Data Elements (CDEs)** for the *ProFound Breast iCAD* dataset.

## Data Elements

### 1. AI Detection Case Score

- **Description:** AI-generated score assessing the likelihood of malignancy.
- **Data Type:** `Integer (0-100)`
- **Range:** `0 to 100`

### 2. Density Assessment

- **Description:** BI-RADS breast density classification.
- **Data Type:** `Float (1.0 - 4.99)`
- **BI-RADS Breast Density:**
  - `1.0 - 1.99` → **A (Very Low)**
  - `2.0 - 2.99` → **B (Scattered)**
  - `3.0 - 3.99` → **C (Heterogeneously Dense)**
  - `4.0 - 4.99` → **D (Extremely Dense)**


---
*Version 1.0 - Maintained by Heather Chase for Microsoft*
