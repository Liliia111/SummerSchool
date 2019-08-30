export const rules = [
    {
        field: 'firstName',
        method: 'isEmpty',
        validWhen: false,
        message: 'First name is required!',
    },
    {
        field: 'firstName',
        method: 'isLength',
        args: [{max: 50}],
        validWhen: true,
        message: 'First name can contain less than 50 char!',
    },
    {
        field: 'lastName',
        method: 'isEmpty',
        validWhen: false,
        message: 'Last name is required!',
    },
    {
        field: 'lastName',
        method: 'isLength',
        args: [{max: 50}],
        validWhen: true,
        message: 'Last name can contain less than 50 char!',
    },
    {
        field: 'email',
        method: 'isEmpty',
        validWhen: false,
        message: 'Email is required!',
    },
    {
        field: 'email',
        method: 'isEmail',
        validWhen: true,
        message: 'That is not a valid email!',
    },
    {
        field: 'password',
        method: 'isEmpty',
        validWhen: false,
        message: 'Password is required!',
    },
    {
        field: 'password',
        method: 'isLength',
        args: [{min: 4, max: 255}],
        validWhen: true,
        message: 'Password must contain more than 4 character and less than 255!',
    },
];