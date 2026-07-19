# 🏁 PitWall

**F1 telemetry analysis platform** — pulling real Formula 1 session data, turning it into race-engineer-grade insights, and serving it through a full API + dashboard stack deployed on Kubernetes.

Built as part of **Stark Lab // DreamHouse LLC** engineering portfolio.

---

## What It Does

PitWall ingests real F1 telemetry (speed, throttle, brake, gear, position — sampled continuously across every lap) and answers the questions a race engineer asks:

- Where is Driver A faster than Driver B, and *why*?
- What do braking zones, throttle traces, and corner speeds reveal about car setup and driving style?
- How does a lap evolve across a session, a stint, or a race weekend?

## Tech Stack

| Layer | Tools | Purpose |
|---|---|---|
| Data | [FastF1](https://github.com/theOehrly/Fast-F1), pandas | Real F1 telemetry ingestion + analysis |
| Visualization | matplotlib → plotly | Speed traces, driver comparisons, track maps |
| API | FastAPI + uvicorn | Serve analysis as REST endpoints |
| Frontend | Streamlit | Interactive dashboard (race/driver selection, live charts) |
| Infra | Docker, K3s | Containerized + deployed on homelab Kubernetes cluster |
| CI/CD | GitHub Actions, ArgoCD | Automated build, test, GitOps deployment |
| Observability | Prometheus, Grafana | Service metrics + monitoring |

## Roadmap

- [x] **Phase 1 — First Lap Trace**: Pull a qualifying lap, plot speed vs. distance
- [ ] **Phase 2 — Driver Comparison**: Overlay two drivers (speed / throttle / brake) + speed-colored track map
- [ ] **Phase 3 — API**: FastAPI backend — sessions, laps, and comparison endpoints
- [ ] **Phase 4 — Dashboard**: Streamlit frontend consuming the PitWall API
- [ ] **Phase 5 — Deploy**: Dockerize → K3s deployment → CI/CD pipeline → Prometheus/Grafana monitoring

## Quick Start

```bash
# Clone and enter the project
git clone https://github.com/<your-username>/pitwall.git
cd pitwall

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create the local data cache (first run downloads session data)
mkdir -p cache

# Run the Phase 1 lap trace
python first_lap.py
```

> **Note:** The first run downloads real session data from the F1 API — give it a minute or two. Subsequent runs load instantly from the local `cache/` folder.

## Project Structure

```
pitwall/
├── cache/           # FastF1 local data cache (gitignored)
├── first_lap.py     # Phase 1: single-lap speed trace
├── requirements.txt # Python dependencies
└── README.md
```

*(Structure grows with each phase — analysis modules, API app, dashboard, and k8s manifests get added as they ship.)*

## Sample Output

*Phase 1 — Verstappen, Monza Qualifying, fastest lap:*

Speed vs. distance trace: plateaus at 330+ km/h are the straights, sharp drops to ~90 km/h are braking zones into the chicanes.

*(Screenshot coming after first run — add yours here!)*

## Why This Project

PitWall is a full-lifecycle engineering exercise: raw data → analysis → API → frontend → containerized deployment with GitOps and monitoring. Every layer runs on infrastructure I built and operate (Stark Lab K3s cluster), demonstrating end-to-end ownership from data pipeline to production ops.

## License

MIT

---

**Built by Rashon | DreamHouse LLC | Stark Lab // Robotics Division**