# WhatsApp AI Accounting Assistant

## Project Overview

The WhatsApp AI Accounting Assistant is an AI-powered accounting system designed to allow small businesses to record, retrieve, and understand their financial transactions using natural language through WhatsApp.

The system combines a WhatsApp interface, an AI agent, a backend application, an accounting engine, and a PostgreSQL database.

## Problem Statement

Many small businesses record financial transactions manually or lack access to simple accounting tools that fit naturally into their existing workflows.

This project aims to provide a conversational accounting assistant through WhatsApp, allowing users to interact with their financial records using ordinary language.

## Core Objective

Build a working prototype that can:

* Receive natural-language financial transactions.
* Interpret transactions using an AI model.
* Validate transaction information.
* Apply double-entry accounting rules.
* Store financial records securely.
* Retrieve balances and financial information.
* Generate basic financial reports.
* Communicate with users through WhatsApp.

## Initial Technology Stack

* **Backend:** Python / FastAPI
* **Package & Environment Management:** uv
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Database Driver:** psycopg
* **AI:** LLM with tool/function calling
* **Messaging:** WhatsApp Business Cloud API
* **Deployment:** To be determined during implementation

## Core Architectural Principle

The AI interprets user messages, but it does not directly control the accounting records.

The intended flow is:

User → AI interpretation → Structured transaction → Validation → Accounting Engine → PostgreSQL

The accounting engine is responsible for applying accounting rules, while PostgreSQL serves as the persistent source of truth.

## Prototype Scope

The first prototype will focus on:

1. User/business setup
2. Chart of accounts
3. Transaction recording
4. Double-entry journal entries
5. Basic financial queries
6. Basic financial reports
7. AI-powered natural-language interaction
8. WhatsApp integration
9. Deployment of the working prototype

## Development Strategy

The project will initially prioritize a working prototype.

After the prototype is completed, the implementation will be reviewed component by component to develop a deeper understanding of the technologies, architecture, accounting logic, and AI techniques used.

## Status

**Current Phase:** Project Setup

**Target:** Working prototype within approximately seven days (a week).
