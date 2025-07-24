import { Routes, Route } from 'react-router-dom';
import Layout from './Layout';
import Home from './pages/Home';
import Sauce from './pages/Sauce';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="sauce/:id" element={<Sauce />} />
      </Route>
    </Routes>
  );
}

export default App;
