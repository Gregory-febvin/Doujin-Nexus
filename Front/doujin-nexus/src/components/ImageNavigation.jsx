// ImageNavigation.jsx
import { useParams, useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import { useSauce } from '../contexts/SauceContext';

export default function ImageNavigation() {
  const { thumbnailNumber } = useParams();
  const navigate = useNavigate();
  const { id, pages } = useSauce();

  const pageNum = parseInt(thumbnailNumber);

  useEffect(() => {
    function handleKeyDown(e) {
      if (e.key === 'ArrowLeft' && pageNum > 1) {
        navigate(`/sauce/${id}/${pageNum - 1}`, { state: { pages } });
      }

      if (e.key === 'ArrowRight' && pageNum < pages) {
        navigate(`/sauce/${id}/${pageNum + 1}`, { state: { pages } });
      }
    }

    window.addEventListener('keydown', handleKeyDown);

    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [navigate]);

  return (
    <div className='navigation-bar'>
      <div className='navigation-bar-left'>
        <div className='back' style={{ cursor: 'pointer' }} onClick={() => navigate(`/sauce/${id}/`, { state: { pages } })}>
          <i className='fa fa-reply' />
        </div>
      </div>
      <div className='navigation-bar-middle'>
        <div className='first-page' style={{ cursor: 'pointer' }} onClick={() => {if (pageNum > 1) navigate(`/sauce/${id}/1`, { state: { pages } });}}>
            <i className='fa fa-chevron-left' />
            <i className='fa fa-chevron-left' />
          </div>
          <div className='previous-page' style={{ cursor: 'pointer' }} onClick={() => {if (pageNum > 1) navigate(`/sauce/${id}/${pageNum - 1}`, { state: { pages } });}}>
            <i className='fa fa-chevron-left' />
          </div>
          <div className='page-number'>
            {thumbnailNumber} / {pages}
          </div>
          <div className='next-page' style={{ cursor: 'pointer' }} onClick={() => {if (pageNum < pages) navigate(`/sauce/${id}/${pageNum + 1}`, { state: { pages } });}}>
            <i className='fa fa-chevron-right' />
          </div>
          <div className='last-page' style={{ cursor: 'pointer' }} onClick={() => {if (pageNum < pages) navigate(`/sauce/${id}/${pages}`, { state: { pages } });}}>
            <i className='fa fa-chevron-right' />
            <i className='fa fa-chevron-right' />
          </div>
    </div>
      <div className='navigation-bar-right'>
        <div></div>
        <div className='reading-parameters'>
          <i className='fa fa-cog' />
        </div>
      </div>
    </div>
  );
}