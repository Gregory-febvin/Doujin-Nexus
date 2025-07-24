import Header from './components/Header';
import Tabs from './components/Tabs';
import { Outlet } from 'react-router-dom';

export default function Layout() {
  return (
    <div className="container">
      <Header />
      <Tabs />
      <div className="content">
        <Outlet />
      </div>
    </div>
  );
}
