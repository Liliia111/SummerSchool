export const rules = [
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