import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import axios from 'axios';
import './AdminPanel.css';

const AdminPanel = () => {
  const { user } = useAuth();
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (user?.role === 'admin') {
      fetchUsers();
    }
  }, [user]);

  const fetchUsers = async () => {
    try {
      setLoading(true);
      const response = await axios.get('/api/admin/users');
      setUsers(response.data.users);
      setError(null);
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to fetch users');
    } finally {
      setLoading(false);
    }
  };

  if (user?.role !== 'admin') {
    return (
      <div className="admin-container">
        <div className="admin-card">
          <h1>Access Denied</h1>
          <p>You need administrator privileges to access this page.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="admin-container">
      <div className="admin-card">
        <div className="admin-header">
          <h1>👑 Admin Panel</h1>
          <button onClick={fetchUsers} className="refresh-button">
            🔄 Refresh
          </button>
        </div>

        {loading && <div className="loading">Loading users...</div>}
        
        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {!loading && !error && (
          <>
            <div className="admin-stats">
              <div className="stat-box">
                <div className="stat-number">{users.length}</div>
                <div className="stat-label">Total Users</div>
              </div>
              <div className="stat-box">
                <div className="stat-number">
                  {users.filter(u => u.role === 'admin').length}
                </div>
                <div className="stat-label">Admins</div>
              </div>
              <div className="stat-box">
                <div className="stat-number">
                  {users.filter(u => u.role === 'user').length}
                </div>
                <div className="stat-label">Regular Users</div>
              </div>
            </div>

            <div className="users-table-container">
              <table className="users-table">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Role</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {users.map((u) => (
                    <tr key={u.id}>
                      <td>#{u.id}</td>
                      <td>{u.name}</td>
                      <td>{u.email}</td>
                      <td>
                        <span className={`role-badge ${u.role}`}>
                          {u.role === 'admin' ? '👑 Admin' : '👤 User'}
                        </span>
                      </td>
                      <td>
                        <button className="action-btn view">View</button>
                        <button className="action-btn edit">Edit</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default AdminPanel;
