import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function Home() {
  const [items, setItems] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/sauces')
      .then(res => res.json())
      .then(data => setItems(data))
      .catch(err => console.error('Erreur:', err));
  }, []);

  return (
    <div className="gallery">
      {items.map(item => (
        <div key={item.id} className="card" onClick={() => navigate(`/sauce/${item.id}`)}>
          <img src={item.cover} alt={`Cover ${item.id}`} />
          <div className="title">{item.title}</div>
        </div>
      ))}
    </div>
  );
}
