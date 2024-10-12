import React, { useState } from 'react';
import {
  MDBContainer,
  MDBInput,
  MDBCheckbox,
  MDBBtn,
  MDBIcon
} from 'mdb-react-ui-kit';

function App({ handleSubmit }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const onSubmit = (e) => {
    e.preventDefault(); // Prevent default form submission
    handleSubmit(email, password); // Call the handleSubmit function with email and password
  };

  return (
    <MDBContainer className="p-3 my-5 d-flex flex-column w-50">
      <form onSubmit={onSubmit}>
        <MDBInput 
          wrapperClass='mb-4' 
          label='Email address' 
          id='form1' 
          type='email' 
          value={email} 
          onChange={(e) => setEmail(e.target.value)} 
        />
        <MDBInput 
          wrapperClass='mb-4' 
          label='Password' 
          id='form2' 
          type='password' 
          value={password} 
          onChange={(e) => setPassword(e.target.value)} 
        />

        <div className="d-flex justify-content-between mx-3 mb-4">
          <MDBCheckbox name='flexCheck' value='' id='flexCheckDefault' label='Remember me' />
          <a href="!#">Forgot password?</a>
        </div>

        <MDBBtn className="mb-4" type="submit">Sign in</MDBBtn>
      </form>

      <div className="text-center">
        <p>Not a member? <a href="#!">Register</a></p>
        <p>or sign up with:</p>

        <div className='d-flex justify-content-between mx-auto' style={{width: '40%'}}>
          <MDBBtn tag='a' color='none' className='m-1' style={{ color: '#1266f1' }}>
            <MDBIcon fab icon='facebook-f' size="sm"/>
          </MDBBtn>

          <MDBBtn tag='a' color='none' className='m-1' style={{ color: '#1266f1' }}>
            <MDBIcon fab icon='twitter' size="sm"/>
          </MDBBtn>

          <MDBBtn tag='a' color='none' className='m-1' style={{ color: '#1266f1' }}>
            <MDBIcon fab icon='google' size="sm"/>
          </MDBBtn>

          <MDBBtn tag='a' color='none' className='m-1' style={{ color: '#1266f1' }}>
            <MDBIcon fab icon='github' size="sm"/>
          </MDBBtn>
        </div>
      </div>
    </MDBContainer>
  );
}

export default App;
