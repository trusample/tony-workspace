# Evidence: 0AMooSbVaWDeSUk9PVA (1lVWgyYksZ7qxx0nSAavUkcbcyIBZgaBLOhwimb7hI1V22Dy2RGWgJFwx)

## File: Code
```

  ]);

  // 04 – Validation
  addSubs(folders["04 – Validation"], [
    "VAL-HbA1c-001 – Validation Plan",
    "External Lab Studies",
    "Usability & IFU Validation",
    "Validation Summary Report"
  ]);

  // 05 – Risk Management
  addSubs(folders["05 – Risk Management"], [
    "RMA-HbA1c-001 – Risk Analysis",
    "FMEA",
    "Risk Control Measures",
    "Residual Risk Evaluation"
  ]);

  // 06 – Stability & Commutability
  addSubs(folders["06 – Stability & Commutability"], [
    "STB-HbA1c-001 – Stability Plan",
    "Real-Time Stability",
    "Accelerated Stability",
    "Commutability Studies",
    "Stability Reports"
  ]);

  // 07 – Design Transfer
  var transfer = addSubs(folders["07 – Design Transfer"], [
    "DMR – Device Master Record",
    "Manufacturing Instructions",
    "QC Release Specifications",
    "Supplier & Component Files"
  ]);

  addSubs(transfer["DMR – Device Master Record"], [
    "Formulation Master",
    "Component Specifications",
    "Filling & Packaging Instructions",
    "Labeling Specifications"
  ]);

  // 08 – Change Control
  addSubs(folders["08 – Change Control"], [
    "Change Requests (ECR)",
    "Change Orders (ECO)",
    "Deviations & Nonconformances",
    "Version History"
  ]);

  // 09 – Regulatory
  addSubs(folders["09 – Regulatory"], [
    "CLIA / LDT Strategy",
    "FDA Strategy",
    "IVDR Strategy",
    "Other Markets",
    "Regulatory Correspondence"
  ]);

  // 10 – Training & Records
  addSubs(folders["10 – Training & Records"], [
    "Training Slides & Materials",
    "Attendance Records",
    "Competency Assessments"
  ]);

  Logger.log("✅ TruSample DHF structure created successfully.");
}
/***********************************************
 * GLOBAL CONFIG – REQUIRED FOR ALL FUNCTIONS
 ***********************************************/
var TS_CONFIG = {
  ROOT_NAME: "TruSample – Synthetic HbA1c Controls (DHF)"
};

/**
 * Build/refresh a DHF_Index tab in the Dashboard
 * Lists all files under the DHF root with lin
```
