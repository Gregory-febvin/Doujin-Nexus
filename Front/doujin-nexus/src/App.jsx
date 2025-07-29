import { Routes, Route } from 'react-router-dom';

import '@fortawesome/fontawesome-free/css/all.min.css';

import Layout from './Layout';
import Home from './pages/Home';
import Sauce from './pages/Sauce';
import ImageFrame from './components/ImageFrame';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="sauce/:id" element={<Sauce />} />
        <Route path="sauce/:id/:thumbnailNumber" element={<ImageFrame />} />
      </Route>
    </Routes>
  );
}

export default App;
