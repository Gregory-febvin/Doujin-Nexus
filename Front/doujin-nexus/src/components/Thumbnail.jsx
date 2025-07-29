// Thumbnail.jsx
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function Thumbnail({ sauce }) {
  const [thumbnailData, setThumbnailData] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    if (sauce) {
      fetch(`http://127.0.0.1:5000/image/${sauce.id}?pages=${sauce.pages}`)
        .then(res => res.json())
        .then(data => setThumbnailData(data))
        .catch(err => console.error('Erreur:', err));
    }
  }, [sauce]);

  if (!thumbnailData) return <p>Chargement...</p>;

  return (
        <div className='thumbnail-container'>
        {thumbnailData.map((url, index) => (
            <div className='thumbnail-image' style={{ cursor: 'pointer' }} onClick={() => navigate(`/sauce/${sauce.id}/${index + 1}`, {state: { pages: sauce.pages }} )}>
                <img className='gallerythumb' loading='lazy' key={index} src={url} alt={`Thumbnail ${index + 1}`} />
            </div>
        ))}
        </div>
  );
}

