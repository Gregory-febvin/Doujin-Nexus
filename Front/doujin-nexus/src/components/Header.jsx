// Header.jsx
import logo from '../assets/logo.png';
import glass from '../assets/glass.svg';

export default function Header() {
  return (
    <div className="header">
      <img className="img-logo" src={logo} alt="Logo Doujin Nexus" />
      <form onSubmit={(e) => e.preventDefault()}>
        <input type="text" className="search-bar" placeholder="Recherche…" />
        <button className="btn btn-search" type="submit">
          <img className="img-search-button" src={glass} alt="Rechercher" />
        </button>
      </form>
    </div>
  );
}

