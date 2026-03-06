import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './Home.css';

const Home = () => {
  const { isAuthenticated } = useAuth();

  return (
    <div className="home-container">
      <div className="hero-section">
        <div className="hero-content">
          <h1 className="hero-title">
            Secure Authentication
            <span className="gradient-text"> Protocol System</span>
          </h1>
          <p className="hero-subtitle">
            Enterprise-grade security with HTTP-only cookies, JWT tokens, and advanced protection mechanisms
          </p>
          <div className="hero-buttons">
            {!isAuthenticated ? (
              <>
                <Link to="/register" className="btn btn-primary">
                  Get Started
                </Link>
                <Link to="/login" className="btn btn-secondary">
                  Sign In
                </Link>
              </>
            ) : (
              <Link to="/dashboard" className="btn btn-primary">
                Go to Dashboard
              </Link>
            )}
          </div>
        </div>
        <div className="hero-image">
          <div className="floating-card card-1">🔒</div>
          <div className="floating-card card-2">🛡️</div>
          <div className="floating-card card-3">🔑</div>
        </div>
      </div>

      <div className="features-section">
        <div className="container">
          <h2 className="section-title">Security Features</h2>
          <div className="features-grid">
            <div className="feature-card">
              <div className="feature-icon">🍪</div>
              <h3>HTTP-Only Cookies</h3>
              <p>Tokens stored securely in HTTP-only cookies, preventing XSS attacks</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">🔐</div>
              <h3>Bcrypt Hashing</h3>
              <p>Industry-standard password encryption with salt</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">🚦</div>
              <h3>Rate Limiting</h3>
              <p>Protection against brute force attacks</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">👑</div>
              <h3>Role-Based Access</h3>
              <p>User and admin roles with protected endpoints</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">🔄</div>
              <h3>Token Refresh</h3>
              <p>Automatic token refresh mechanism</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon">✅</div>
              <h3>Input Validation</h3>
              <p>Comprehensive validation and sanitization</p>
            </div>
          </div>
        </div>
      </div>

      <div className="stats-section">
        <div className="container">
          <div className="stats-grid">
            <div className="stat-item">
              <div className="stat-number">100%</div>
              <div className="stat-label">Secure</div>
            </div>
            <div className="stat-item">
              <div className="stat-number">24/7</div>
              <div className="stat-label">Protection</div>
            </div>
            <div className="stat-item">
              <div className="stat-number">Enterprise</div>
              <div className="stat-label">Grade</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
