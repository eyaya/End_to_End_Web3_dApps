import React, { Component } from 'react';
import axios from "axios";

class App extends Component {
  state = {
    Accounts: []
  };
  
  
  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/'); // fetching the data from api, before the page loaded
      const Accounts = await res.json();
      this.setState({
        Accounts
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.Accounts.map(item => (
          <div key={item.address}>
            <h1>{item.private_key}</h1>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
