import React from 'react';

const EpicList = ({epics}) => (
    <div>
        <h2>Here is your list!</h2>
        {
            epics.map(({ id, description, taskSet }) => (
                <div key={id}>
                    <h2>{`Epic # ${id}`}</h2>
                    <p>{description}</p>
                    <ul>
                        {taskSet.map(({id, name}) => (<li key={id}>{name}</li>))}
                    </ul>
                </div>
            ))
        }
    </div>
);

export default EpicList;