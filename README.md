# Aegis Sentinel

[![Python Version](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/PkLavc/aegis-sentinel?style=social)](https://github.com/PkLavc/aegis-sentinel)

## Executive Summary

Aegis Sentinel is a high-reliability infrastructure monitoring and auto-healing engine designed to ensure business continuity and infrastructure resilience in enterprise environments. This system implements advanced anomaly detection algorithms and automated recovery mechanisms to prevent catastrophic downtime in digital services.

The platform demonstrates advanced engineering principles suitable for international standards, particularly aligned with EB-2 NIW requirements for demonstrating exceptional ability in systems engineering and infrastructure automation.

## Engineering Specifications

### Technical Architecture

Aegis Sentinel employs a modular, service-oriented architecture with three core components:

1. **Monitor Service**: Real-time system metrics collection
2. **ML-Anomaly Detection**: Machine learning-based anomaly identification
3. **Recovery Engine**: Automated remediation and healing actions

### Core Technologies

- **Python 3.11+** with strict type hinting
- **Structured JSON logging** for enterprise auditability
- **Isolation Forest** and statistical anomaly detection
- **Docker container management** for automated recovery
- **Comprehensive testing** with pytest framework

### Visual Workflow
```mermaid
graph LR
    A[Metrics Collection] --> B[ML Detection]
    B --> C{Anomaly?}
    C -- No --> A
    C -- Yes --> D[Recovery Engine]
    D --> E[Self-Healing Action]
```

### System Requirements

- Python 3.11 or higher
- Docker (for containerized recovery actions)
- Standard Python libraries: psutil, numpy, scikit-learn
- Optional: Redis for distributed caching

## National Interest Context

In today's digital economy, infrastructure reliability is critical for maintaining essential services. Aegis Sentinel addresses the national interest by:

- **Preventing catastrophic downtime** in critical digital infrastructure
- **Reducing economic impact** of system failures through rapid automated recovery
- **Enhancing cybersecurity resilience** through proactive anomaly detection
- **Demonstrating technological leadership** in infrastructure automation

### Engineering Impact Metrics
| Metric | Target | National Interest Benefit |
| :--- | :--- | :--- |
| **Detection Latency** | < 2.0s | Real-time response to critical failures |
| **False Positive Rate** | < 5% | Minimizes operational disruption |
| **Recovery Success** | > 95% | Ensures high availability for essential services |

The system's ability to detect and remediate issues before they escalate to service outages directly contributes to the stability and reliability of digital services that are essential to modern society.

## Installation

```bash
pip install -r requirements.txt
```

> **Personal note:** I'm running this on a home lab with limited RAM, so I set the Isolation Forest `n_estimators` to 50 (down from the default 100) to reduce memory usage. Works fine for my single-node setup.
