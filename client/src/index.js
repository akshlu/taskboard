import React from 'react';
import ReactDOM from 'react-dom';
import Root from './Root';
import ApolloClient from 'apollo-boost';
import { ApolloProvider } from 'react-apollo';

const client = new ApolloClient({
    uri: 'http://localhost:1337/graphql',
});

const App = () => {
    return (
        <ApolloProvider client={client}>
            <Root/>
        </ApolloProvider>
    );
};

ReactDOM.render(<App />, document.getElementById('app'));