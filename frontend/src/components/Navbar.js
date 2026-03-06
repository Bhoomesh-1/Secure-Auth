import React from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './Navbar.css';

const Navbar = () => {
  const { user, isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogout = async () => {
    await logout();
    navigate('/');
  };

  const isActive = (path) => {
    return location.pathname === path ? 'active' : '';
  };

  if (!isAuthenticated) {
    return (
      <nav className="navbar">
        <div className="navbar-container">
          <Link to="/" className="navbar-logo">
            <span className="logo-icon">🔐</span>
            SecureAuth
          </Link>
          <div className="navbar-menu">
            <Link to="/" className={`navbar-link ${isActive('/')}`}>
              Home
            </Link>
            <Link to="/about" className={`navbar-link ${isActive('/about')}`}>
              About
            </Link>
            <Link to="/login" className="navbar-link navbar-button">
              Login
            </Link>
            <Link to="/register" className="navbar-link navbar-button-primary">
              Sign Up
            </Link>
          </div>
        </div>
      </nav>
    );
  }

  return (
    <nav className="navbar" aria-label="Main Navigation">
      <div className="navbar-container">
        <Link to="/dashboard" className="navbar-logo" aria-label="Go to Dashboard">
          <span className="logo-icon" role="img" aria-label="SecureAuth Logo">🔐</span>
          SecureAuth
        </Link>
        <div className="navbar-menu" role="navigation">
          <Link to="/dashboard" className={`navbar-link ${isActive('/dashboard')}`} aria-current={isActive('/dashboard') ? 'page' : undefined}>
            Dashboard
          </Link>
          <Link to="/security" className={`navbar-link ${isActive('/security')}`} aria-current={isActive('/security') ? 'page' : undefined}>
            Security
          </Link>
          <Link to="/profile" className={`navbar-link ${isActive('/profile')}`} aria-current={isActive('/profile') ? 'page' : undefined}>
            Profile
          </Link>
          <Link to="/settings" className={`navbar-link ${isActive('/settings')}`} aria-current={isActive('/settings') ? 'page' : undefined}>
            Settings
          </Link>
          {user?.role === 'admin' && (
            <Link to="/admin" className={`navbar-link ${isActive('/admin')}`} aria-current={isActive('/admin') ? 'page' : undefined}>
              Admin
            </Link>
          )}
          <div className="navbar-user">
            <span className="user-name" aria-label="Logged in user">{user?.name}</span>
            <button onClick={handleLogout} className="navbar-logout" aria-label="Logout">
              Logout
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
