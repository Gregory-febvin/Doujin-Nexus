// Sauce.jsx
import { Route, useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import Infos from '../components/Infos';
import Thumbnail from '../components/Thumbnail';

export default function Sauce() {
  const { id } = useParams();
  const [sauce, setSauce] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/api/sauce/${id}`)
      .then(res => res.json())
      .then(data => setSauce(data))
      .catch(err => console.error('Erreur:', err));
  }, [id]);

  return (
  <div className='sauce'>
    <Infos sauce={sauce} />
    <Thumbnail sauce={sauce}/>
  </div>
  );
}

