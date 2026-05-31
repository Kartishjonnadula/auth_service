# Auth Service

A production-inspired authentication service built with FastAPI, PostgreSQL, SQLAlchemy, JWT (RS256), and Refresh Token Rotation.

This project was built as a personal learning exercise to understand how modern authentication systems work internally, rather than relying on managed identity providers such as Keycloak, Auth0, Cognito, or Okta.

## Features

### Authentication

- User Registration
- User Login
- Password Hashing using bcrypt
- JWT Access Tokens (RS256)
- Protected Endpoints
- Current User Resolution

### Session Management

- Refresh Tokens
- Refresh Token Persistence in PostgreSQL
- Refresh Token Rotation
- Token Expiration
- Logout Support

### Architecture

- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Repository Pattern
- Service Layer Pattern
- Dependency Injection using FastAPI Depends

## Learning Goals

- FastAPI fundamentals
- Dependency Injection
- SQLAlchemy
- Repository Pattern
- Service Layer Architecture
- JWT Authentication
- RS256 Public/Private Key Cryptography
- Session Management
- Refresh Token Rotation
- Production Authentication Design

## Future Improvements

- Alembic Migrations
- Device Tracking
- Session Management APIs
- Login History
- RBAC
- Email Verification
- Password Reset Flow
- MFA
- OAuth Providers

## Disclaimer

This project is a personal learning project intended to explore authentication system design and backend architecture concepts. It is not intended to be used directly in production without additional hardening, testing, monitoring, and security review.
