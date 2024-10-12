import React, { useState } from "react";
import {
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBCard,
  MDBCardBody,
  MDBIcon,
  MDBBtn,
  MDBTypography,
  MDBTextArea,
  MDBCardHeader,
} from "mdb-react-ui-kit";
import Login from './Login'; // Make sure the path is correct

export default function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false); // State to track if the user is logged in

  // This function would be called upon successful login
  const handleLogin = () => {
    setIsAuthenticated(true); // Set authenticated state to true
  };

  return (
    <MDBContainer fluid className="py-5" style={{ backgroundColor: "#eee" }}>
      {!isAuthenticated ? (
        <Login onLogin={handleLogin} /> // Render login if not authenticated
      ) : (
        <MDBRow>
          <MDBCol md="6" lg="5" xl="4" className="mb-4 mb-md-0">
            <h5 className="font-weight-bold mb-3 text-center text-lg-start">
              Member
            </h5>
            <MDBCard>
              <MDBCardBody>
                <MDBTypography listUnStyled className="mb-0">
                  {/* Your list of members as before */}
                </MDBTypography>
              </MDBCardBody>
            </MDBCard>
          </MDBCol>

          <MDBCol md="6" lg="7" xl="8">
            <MDBTypography listUnStyled>
              {/* Your chat functionality as before */}
              <li className="bg-white mb-3">
                <MDBTextArea label="Message" id="textAreaExample" rows={4} />
              </li>
              <MDBBtn color="info" rounded className="float-end">
                Send
              </MDBBtn>
            </MDBTypography>
          </MDBCol>
        </MDBRow>
      )}
    </MDBContainer>
  );
}
