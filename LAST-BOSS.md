## eBay Scraper Project with FastAPI and Typer
Project Overview
A dual-interface application that combines FastAPI for web API and Typer for CLI operations to scrape and manage eBay product data.

## Core Features
1. Web API Interface (FastAPI)
Product search endpoints
Data export functionality
Product detail retrieval
2. CLI Interface (Typer)
Command-line operations:

3. Data Collection
Product Name
Price Information
Product Specifications
eBay Item Number
4. Export Capabilities
CSV format export
Excel (.xlsx) export
Filtered data export
CLI Commands
Main Commands
search - Search for products on eBay

Options:
`--limit: Number of results`
`--category: Filter by category`
`--sort: Sort results`
`export - Export scraped data`

Options:
`--format: csv/excel`
`--output: Output filename`
`--query: Filter results`
`product - Get specific product details`

Options:
`--item-number: eBay item number`
`--save: Save to file`
`--output: Output filename`

## Technical Features
Rich console output for CLI
Progress bars for long operations
Colorized terminal output
Command auto-completion
Interactive CLI prompts
Error handling and logging
Data validation
# DEADLINE: 2025-08-29
# PROJECT: eBay Scraper
