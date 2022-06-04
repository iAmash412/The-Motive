import React from 'react';
import introGif from '../../images/intro.gif';
import TypeWriterEffect from 'react-typewriter-effect';

const LandingPage = () => {
  // const { text } = useTypewriter({
  //     words: ['for those who thrive in spontaneity, the.MOTIVE is your way to continue the night'],
  //     loop: 0
  // });

  return (
    <div className="main-container">
      <div className="image-container">
        <img src={introGif} alt="Intro Gif" />
        <div className="typewriter">
          <TypeWriterEffect
            textStyle={{
              fontFamily: 'monospace',
              fontWeight: 500,
              fontSize: '1.5em',
              color: '#ff5900',
            }}
            cursorColor="#ff5900"
            multiText={[
              'for those',
              'who thrive in spontaneity',
              'the.MOTIVE is your way',
              'to continue the night',
            ]}
            typeSpeed={100}
            startDelay={0.5}
            nextTextDelay={0.5}
            loop={true}
          />
          {/* <h1 className='typing-effect'>
                       {text} <Cursor cursorStyle='_' />
                    </h1> */}
        </div>
      </div>
      <div>
        <a href="/Login">
          <button>Login</button>
        </a>
        <a href="/Register">
          <button>Register</button>
        </a>
      </div>
    </div>
  );
};

export default LandingPage;
