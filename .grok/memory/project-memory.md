# Stock Options & Short Interest Monitor
## Project Plan

### 1. Overview

This project is a web application that monitors stock prices, options activity (Calls and Puts volume by expiration), and short selling data. The system automatically collects daily data for any stock entered by the user and stores the full historical data in the database.

**Key Features:**
- Daily automated data collection for stocks, options chains, and short interest.
- Interactive React frontend with multiple charts.
- Ability to overlay and compare two stocks on the same chart.
- Historical data storage from the first time a stock is added.
- Focus on options volume by expiration date and short selling metrics.

### 2. Technology Stack & Architecture

**High-level Architecture (Modular by Design)**

The project is structured from day one to support future growth and separation:

- **Monorepo initially** with clear boundaries (`/backend` and `/frontend` folders)
- Backend and Frontend communicate **exclusively via REST API** (OpenAPI/Swagger)
- No shared business logic between frontend and backend
- Each part can be extracted into its own repository later with minimal effort
- Docker Compose runs backend and frontend as independent services

**Backend:**
- Python 3.11+
- FastAPI (main web framework)
- Celery + Redis (for daily scheduled tasks)
- SQLAlchemy + Alembic (ORM and migrations)
- PostgreSQL (primary database)
- yfinance + custom scrapers (data sources)
- Polygon.io or Barchart (optional premium data sources)

**Frontend:**
- React 18+ with TypeScript
- Tailwind CSS or Material-UI
- Recharts or Chart.js + D3.js (for interactive charts)
- TanStack Query (for data fetching)
- Date-fns or dayjs (date handling)

**Infrastructure:**
- Docker + Docker Compose (all services containerized from day one)
- PostgreSQL database running inside Docker container
- Redis running inside Docker container (Celery broker + cache)
- Deployment: Railway, Render, or AWS (Docker-based)

### 3. Database Schema (Designed based on yfinance API)

The schema is designed to store complete historical data from yfinance while supporting efficient querying for options by expiration and short interest.

#### Core Tables

**stocks**
- id (PK)
- ticker (unique, indexed)
- company_name
- sector
- industry
- market_cap
- created_at
- updated_at

**stock_prices_daily**
- id (PK)
- stock_id (FK → stocks)
- date (date, indexed)
- open
- high
- low
- close
- volume
- adj_close
- UNIQUE(stock_id, date)

**options_chains**
- id (PK)
- stock_id (FK)
- expiration_date (date, indexed)
- option_type ('call' or 'put')
- strike
- last_price
- bid
- ask
- volume
- open_interest
- implied_volatility
- date_collected (date when data was scraped)
- UNIQUE(stock_id, expiration_date, option_type, strike, date_collected)

**options_daily_summary**
- id (PK)
- stock_id (FK)
- date (date, indexed)
- total_call_volume
- total_put_volume
- put_call_ratio
- total_call_oi
- total_put_oi
- UNIQUE(stock_id, date)

**short_interest**
- id (PK)
- stock_id (FK)
- date (date, indexed)
- short_volume
- short_percent_of_float
- days_to_cover
- short_interest_shares
- UNIQUE(stock_id, date)

**stock_metadata**
- id (PK)
- stock_id (FK)
- info_json (JSONB)          -- full yfinance .info
- history_start_date
- last_updated

### 4. Data Collection Strategy

When a user adds a new stock (ticker):
1. Immediately fetch full historical price data from yfinance (`period="max"`)
2. Fetch current options chain for all available expirations
3. Fetch short interest data (via yfinance or alternative source)
4. Store everything in the database
5. Schedule daily updates via Celery

Daily task (runs after US market close):
- Update price for all tracked stocks
- Update options chain + volume for active expirations
- Update short interest (if new data available)

### 5. Frontend (React) Requirements

**Main Pages / Views:**

1. **Dashboard**
   - List of tracked stocks
   - Quick stats (latest price, daily change, Put/Call ratio)

2. **Stock Detail Page**
   - **Chart 1: Stock Price + Volume**
     - Interactive candlestick or line chart with volume bars
     - Time range selector (1M, 3M, 6M, 1Y, Max, Custom)

   - **Chart 2: Options Activity**
     - Stacked bar or area chart showing daily total Call Volume vs Put Volume
     - Second view: Options volume grouped by expiration date (heatmap or grouped bars)
     - Short Interest overlay (dual axis)

3. **Comparison View (Key Feature)**
   - Select two stocks (Stock A vs Stock B)
   - **Overlay Chart** with the following capabilities:
     - Time interval selector
     - Toggle between:
       - Price comparison (normalized or absolute)
       - Put/Call Ratio comparison
       - Total Options Volume comparison
       - Short Interest comparison
     - Ability to filter by specific expiration dates for options
     - Synchronized zooming and tooltips

**Technical Frontend Notes:**
- Use Recharts or Chart.js with plugins for interactivity
- Implement date range picker
- Responsive design (mobile friendly)
- Dark mode support recommended

### 6. Project Phases

#### Phase 1: Foundation & Modular Architecture (2–3 weeks)
- Set up **modular monorepo structure** with clear separation:
  - `/backend` (FastAPI + Celery)
  - `/frontend` (React)
  - Shared Docker Compose with independent services
- Configure Docker Compose to start **PostgreSQL** and **Redis** containers
- Define strict API contract using OpenAPI (FastAPI auto-generates it)
- Implement database schema and migrations (running against Docker PostgreSQL)
- Create basic yfinance data ingestion script (full history on first stock add)
- Build Celery task for daily price updates
- Simple React frontend with stock search + price chart (consumes backend API only)
- User can add a stock and see historical price data

**Goal of this phase:** Establish an architecture that allows the frontend to be moved to its own repository and the backend to be split into multiple services (e.g. data-ingestion service, API service) in the future with minimal refactoring.

#### Phase 2: Options Data & Basic Charts (3–4 weeks)
- Implement full options chain scraping + storage (all expirations)
- Create `options_daily_summary` table and daily aggregation
- Build second interactive chart: Call vs Put volume + Put/Call ratio
- Add short interest data collection
- Improve React frontend with two main charts on stock detail page
- Basic filtering by expiration date

#### Phase 3: Advanced Comparison & Analytics (3–4 weeks)
- Develop the **Comparison View** with overlay capabilities
- Implement advanced filtering:
  - Time range synchronization
  - Expiration date selection for options overlay
  - Normalized price comparison
- Add more analytics (e.g., unusual options activity detection)
- Improve UI/UX and responsiveness
- Add export functionality (CSV)

#### Phase 4: Polish, Alerts & Deployment (2–3 weeks)
- User authentication (optional)
- Email / Telegram alerts for unusual volume or short interest spikes
- Performance optimization (indexing, caching)
- Full Docker deployment setup
- Documentation and README
- Production deployment (Railway / Render / AWS)

### 7. Future Enhancements (Post v1.0)

- Real-time data via WebSockets (if using premium APIs)
- Machine learning model to predict unusual options activity
- Portfolio tracking
- Mobile app (React Native)
- Integration with Interactive Brokers or other brokers

### 8. Risks & Considerations

- yfinance has rate limits → implement caching and respectful scraping
- Options data can be very large → proper indexing and partitioning by date
- Short interest data is not always daily → handle missing data gracefully
- Frontend performance with large date ranges → use data aggregation / downsampling

---

**Next Step:**  
Would you like me to start creating the actual files (Docker setup, database models, basic FastAPI structure, or React components)? Or should I expand any specific phase?