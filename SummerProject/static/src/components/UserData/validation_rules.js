export const rules = [
    {
        field: 'firstName',
        method: 'isLength',
        args: [{max: 50}],
        validWhen: true,
        message: 'First name can contain less than 50 char!',
    },
    {
        field: 'lastName',
        method: 'isLength',
        args: [{max: 50}],
        validWhen: true,
        message: 'Last name can contain less than 50 char!',
    },
];