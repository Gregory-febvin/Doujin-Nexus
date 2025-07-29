// Infos.jsx
import { useNavigate } from 'react-router-dom';

export default function Infos({sauce}) {
  const navigate = useNavigate();

  if (!sauce) return <p>Chargement...</p>;

  return (
   <div className='infos-container'>
        <div id='main-cover'>
            <img className='cover-image' loading='lazy' src={sauce.cover} alt={sauce.title} 
            rel='nofollow' style={{ cursor: 'pointer' }} onClick={() => navigate(`/sauce/${sauce.id}/1`)}/>
        </div>
        <div id='main-infos'>
            <div className='sauce-title data-fields'>
                <h1 className='title'>{sauce.title}</h1>
            </div>

            <div className='sauce-id data-fields'>
                <h3 className='galleries-id'>{sauce.id}</h3>
            </div>

            {(sauce.parodies && sauce.parodies.trim()) && (
            <div className='sauce-parodies data-fields'>
                {'Parodies: '}
                <span className='tags'>
                {sauce.parodies.split(',').map((parody, index) => (
                    <a key={index} className='tag' href={`/parodies/${parody.trim()}`}>
                    <span className='name'>{parody.trim()}</span>
                    <span className='count'>35K</span>
                    </a>
                ))}
                </span>
            </div>
            )}


            <div className='sauce-character data-fields'>

            </div>

            {(sauce.tags && sauce.tags.trim()) && (
            <div className='sauce-tags data-fields'>
                {'Tags: '}
                <span className='tags'>
                {sauce.tags.split(',').map((tag, index) => (
                    <a key={index} className='tag' href={`/tag/${tag.trim()}`}>
                    <span className='name'>{tag.trim()}</span>
                    <span className='count'>35K</span>
                    </a>
                ))}
                </span>
            </div>
            )}


            {(sauce.artists && sauce.artists.trim()) && (
            <div className='sauce-artists data-fields'>
                {'Artists: '}
                <span className='tags'>
                {sauce.artists.split(',').map((tag, index) => (
                    <a key={index} className='tag' href={`/artist/${tag.trim()}`}>
                    <span className='name'>{tag.trim()}</span>
                    <span className='count'>35K</span>
                    </a>
                ))}
                </span>
            </div>
            )}

            {(sauce.groups && sauce.groups.trim()) && (
            <div className='sauce-groups data-fields'>
                {'Groups: '}
                <span className='tags'>
                {sauce.groups.split(',').map((tag, index) => (
                    <a key={index} className='tag' href={`/group/${tag.trim()}`}>
                    <span className='name'>{tag.trim()}</span>
                    <span className='count'>35K</span>
                    </a>
                ))}
                </span>
            </div>
            )}

            {(sauce.languages && sauce.languages.trim()) && (
            <div className='sauce-languages data-fields'>
                {'Languages: '}
                <span className='tags'>
                {sauce.languages.split(',').map((tag, index) => (
                    <a key={index} className='tag' href={`/language/${tag.trim()}`}>
                    <span className='name'>{tag.trim()}</span>
                    <span className='count'>35K</span>
                    </a>
                ))}
                </span>
            </div>
            )}

            {(sauce.categories && sauce.categories.trim()) && (
            <div className='sauce-languages data-fields'>
                {'Categories: '}
                <span className='tags'>
                {sauce.categories.split(',').map((tag, index) => (
                    <a key={index} className='tag' href={`/category/${tag.trim()}`}>
                    <span className='name'>{tag.trim()}</span>
                    <span className='count'>35K</span>
                    </a>
                ))}
                </span>
            </div>
            )}

            {(sauce.pages && sauce.pages > 0) && (
            <div className='sauce-pages data-fields'>
                {'Pages: '}
                <span className='tags'>
                <a className='tag'>
                    <span className='name'>{sauce.pages}</span>
                </a>
                </span>
            </div>
            )}
        </div>
   </div>
  );
}