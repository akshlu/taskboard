import gql from 'graphql-tag';

export const getAllEpicsWithTasksQuery = gql`
    {
        epics {
            id
            description
            taskSet {
                id
                name
            }
        }
    }
`;