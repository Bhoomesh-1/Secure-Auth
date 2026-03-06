import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './About.css';

const About = () => {
  const { isAuthenticated } = useAuth();

  return (
    <div className="about-container">
      <div className="about-hero">
        <h1>About Secure Authentication</h1>
        <p>Enterprise-grade security protocol system</p>
      </div>

      <div className="about-content">
        <div className="about-section">
          <h2>Our Mission</h2>
          <p>
            To provide a secure, scalable, and user-friendly authentication system
            that protects user data with industry-standard security practices.
          </p>
        </div>

        <div className="about-section">
          <h2>Security Features</h2>
          <div className="features-list">
            <div className="feature-item">
              <span className="feature-icon">🔒</span>
              <div>
                <h3>HTTP-Only Cookies</h3>
                <p>Tokens stored securely, preventing XSS attacks</p>
              </div>
            </div>
            <div className="feature-item">
              <span className="feature-icon">🛡️</span>
              <div>
                <h3>Bcrypt Password Hashing</h3>
                <p>Industry-standard encryption with salt</p>
              </div>
            </div>
            <div className="feature-item">
              <span className="feature-icon">🚦</span>
              <div>
                <h3>Rate Limiting</h3>
                <p>Protection against brute force attacks</p>
              </div>
            </div>
            <div className="feature-item">
              <span className="feature-icon">👑</span>
              <div>
                <h3>Role-Based Access</h3>
                <p>User and admin role management</p>
              </div>
            </div>
          </div>
        </div>

        <div className="about-section">
          <h2>Technology Stack</h2>
          <div className="tech-grid">
            <div className="tech-item">React</div>
            <div className="tech-item">Flask</div>
            <div className="tech-item">JWT</div>
            <div className="tech-item">Bcrypt</div>
            <div className="tech-item">Axios</div>
            <div className="tech-item">Python</div>
          </div>
        </div>

        <div className="about-section">
          <h2>Get Started</h2>
          <p>Ready to secure your application?</p>
          <div className="cta-buttons">
            {!isAuthenticated ? (
              <>
                <Link to="/register" className="cta-button primary">
                  Create Account
                </Link>
                <Link to="/login" className="cta-button secondary">
                  Sign In
                </Link>
              </>
            ) : (
              <Link to="/dashboard" className="cta-button primary">
                Go to Dashboard
              </Link>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;
