
create table IF NOT EXISTS tasks
(
    TaskId integer primary key,
    Title text not null,
    Detail text not null,
    Done integer not null,
    Position real null,
    GoDaddyId integer null,
    Contexts text null,
    Due real null
);

