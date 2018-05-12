import React from 'react';
import { Query } from 'react-apollo';
import { getAllEpicsWithTasksQuery } from './queries';

import EpicList from './EpicList';

const Root = () => (
    <div>
        <h1>Hello from React!</h1>
        <Query query={getAllEpicsWithTasksQuery}>
            {({ loading, error, data }) => {
                
                if (loading) return <p>Loading...</p>;
                if (error) return <p>Error :(</p>;

                return <EpicList epics={data.epics}/>;

            }}
        </Query>
    </div> 
);

export default Root;