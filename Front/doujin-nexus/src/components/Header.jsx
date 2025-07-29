// Header.jsx
import { useNavigate } from 'react-router-dom';

import logo from '../assets/logo.png';
import glass from '../assets/glass.svg';

export default function Header() {
  const navigate = useNavigate();

  return (
    <div className="header">
      <img className="img-logo" src={logo} alt="Logo Doujin Nexus" style={{ cursor: 'pointer' }} onClick={() => navigate(`/`)}/>
      <form onSubmit={(e) => e.preventDefault()}>
        <input type="text" className="search-bar" placeholder="Recherche…" />
        <button className="btn btn-search" type="submit">
          <i className="fa fa-search fa-lg" />
        </button>
      </form>
    </div>
  );
}

