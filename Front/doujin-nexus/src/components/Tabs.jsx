// Tabs.jsx
import { useNavigate } from 'react-router-dom'

export default function Header() {
  const navigate = useNavigate();

  return (
    <div className="tabs">
        <div className="link">
            <div className="tab"><a style={{ cursor: 'pointer' }} onClick={() => navigate(`/random`)}>Aléatoire</a></div>
            <div className="tab"><a style={{ cursor: 'pointer' }} onClick={() => navigate(`/parodies`)}>Séries</a></div>
            <div className="tab"><a style={{ cursor: 'pointer' }} onClick={() => navigate(`/tags`)}>Tags</a></div>
            <div className="tab"><a style={{ cursor: 'pointer' }} onClick={() => navigate(`/characters`)}>Personnages</a></div>
            <div className="tab"><a style={{ cursor: 'pointer' }} onClick={() => navigate(`/artists`)}>Artistes</a></div>
            <div className="tab"><a style={{ cursor: 'pointer' }} onClick={() => navigate(`/groups`)}>Groupes</a></div>
            <div className="tab"><a style={{ cursor: 'pointer' }} onClick={() => navigate(`/info`)}>Aide</a></div>
        </div>
    </div>
  );
}
