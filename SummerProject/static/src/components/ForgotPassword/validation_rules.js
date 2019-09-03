export const rules = [
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
    }
];