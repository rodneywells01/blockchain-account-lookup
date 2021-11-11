import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [currentMessage, setCurrentMessage] = useState(0);
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

class AccountInput extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      account_id: '',
      value: 0,
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    console.log(event.target.value);
    this.setState({account_id: event.target.value});
  }

  handleSubmit(event) {
    // alert('An account_id was submitted: ' + this.state.account_id);
    event.preventDefault();

    fetch('/sol/' + this.state.account_id).then(res => res.json()).then(data => {
      console.log("Got it!")
      console.log(data);
      this.setState({value: data.sol_balance});
    });
  }

  // 6sFdGABSP5FA3Lx8i473zBeEGn5uAS7h7wprwj9nWVaz

  render() {
    if (this.state.value) {
      return (
        <div className="verticalbuffer">
          <form onSubmit={this.handleSubmit}>
            <label>
              SOL Account ID:
              <input type="text" name="account_id" value={this.state.account_id} onChange={this.handleChange} />
            </label>
            <input type="submit" value="Submit" />
          </form>
          <div id="value_display">
            You own: {this.state.value} SOL
          </div>
        </div>
      )
    } else {
      return (
        <div className="verticalbuffer">
          <form onSubmit={this.handleSubmit}>
            <label>
              SOL Account ID:
              <input type="text" name="account_id" value={this.state.account_id} onChange={this.handleChange} />
            </label>
            <input type="submit" value="Submit" />
          </form>
        </div>
      )
    }

    
  }
}

class MyApp extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  }

  render () {
    return (
      <div id="background">
        <div id="greeting-card">
          <div id="pantry-text">
            <h1>Crypto Net Worth Tracker</h1>
          </div>
          <div id="greeting">
            <h3>Time to track your net worth.</h3>
          </div>
        </div>
      
        <AccountInput/>
      </div>
    );

  }

}
export default MyApp;
// export default App;