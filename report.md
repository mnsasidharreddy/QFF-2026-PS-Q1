# QFF 2026 PS-Q1 — Phase 1 Report

## 1. Specification
This implementation follows the earlier PS-Q1 brief: 200 synthetic samples, four features, binary classes, a four-qubit VQC, and an 80/20 split. The later consolidated guide describes an ECG/EEG version. Record organizer clarification here before final submission.

## 2. Dataset and preprocessing
Generator: `make_classification`; 200 samples; 4 features; 3 informative; 0 redundant; seed 42; stratified 80/20 split. `MinMaxScaler` is fit only on training data and maps features to [-1, 1].

## 3. Model
Describe angle encoding, trainable rotations, entangling gates, measured output, loss, optimizer, and stopping criteria.

## 4. Processor A/B configurations
Document coupling maps, basis gates, transpiler settings, and authoritative specification source.

## 5. Results
Insert measured outputs from `results/tables/processor_comparison.csv`. Do not invent results.

## 6. Analysis
Compare accuracy and loss; explain depth, CX, and SWAP differences. The same logical circuit/sample is compiled for A and B.

## 7. Limitations
Training uses an ideal statevector. The current benchmark measures compiled circuit resources; it does not claim noisy A/B classification accuracy.

## 8. Reproducibility and AI disclosure
Record package versions, seeds, and execution steps. Follow the hackathon AI-use policy and disclose assistance if required.
