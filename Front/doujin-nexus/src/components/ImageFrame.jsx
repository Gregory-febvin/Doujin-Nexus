import { useParams, useLocation } from 'react-router-dom';
import { useEffect, useRef } from 'react';
import { SauceContext } from '../contexts/SauceContext';
import ImageNavigation from './ImageNavigation';

export default function ImageFrame() {
  const { id, thumbnailNumber } = useParams();
  const location = useLocation();
  const imageRef = useRef(null);

  const pages = location.state?.pages ?? 1;

  const imageUrl = `http://127.0.0.1:5000/image/${id}/${thumbnailNumber}`;

  useEffect(() => {
    if (imageRef.current) {
      imageRef.current.scrollIntoView({ behavior: 'auto', block: 'center' });
    }
  }, []);

  return (
    <SauceContext.Provider value={{ id, pages }}>
      <ImageNavigation />
      <img
        ref={imageRef}
        style={{ height: '100vh', width: 'auto', display: 'block', margin: 'auto' }}
        src={imageUrl}
        alt={`Thumbnail ${thumbnailNumber}`}
      />
      <ImageNavigation />
    </SauceContext.Provider>
  );
}
