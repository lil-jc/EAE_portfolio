-- Keep a log of any SQL queries you execute as you solve the mystery.

-- theft took place on July 28, 2021 and it took place on Humphrey Street.

--look in to the crime_reports
SELECT *
FROM crime_scene_reports
WHERE year = 2021
AND month = 7
AND day = 28
AND street ='Humphrey Street';
-- found that the 3 interviewers have all mentioned a bakery
-- crime took place at 10.15am


-- look into the interviews
select *
from interviews
where year = 2021
and month = 7
and day = 28
and transcript like '%bakery%';
-- left the place with car at within 10 min
-- thieve widthdraw money on Leggett Street earlier that morning
-- made a phone call less than minute, taking earliest flight out of Fiftyville the next day(july 29 2021)


-- look into the carpark security log to list suspects
SELECT name
from people
where license_plate
IN(
    select license_plate
    from bakery_security_logs
    where year = 2021
    AND month = 7
    AND day =28
    AND activity = 'exit'
    AND hour = 10
)
ORDER BY name;
-- Barry
-- Bruce
-- Diana
-- Iman
-- Kelsey
-- Luca
-- Sofia
-- Taylor
-- Vanessa


-- look into amt_transactions
SELECT name
from people
WHERE id
IN(
    select person_id
    from bank_accounts join atm_transactions on bank_accounts.account_number = atm_transactions.account_number
    where year = 2021
    AND month = 7
    AND day = 28
    AND transaction_type = 'withdraw'
)
order by name;
-- Bruce
-- Diana
-- Iman
-- Luca
-- Taylor


-- find earliest flight out of fiftyville on july 29 2021
select *
from flights
where year = 2021
and month = 7
and day = 29
and origin_airport_id = 8
order by (hour)
limit 1;
-- destination_airport_id = 4
-- flight_id = 36


-- check where they are going to
select *
from airports
where id = 4
-- New York City


-- check check passenger names
select name
from people
where passport_number
IN(
    select passport_number
    from passengers
    where flight_id = 36
)
order by name;
-- Bruce
-- Luca
-- Taylor


--check the phone number of each person
select *
from people
where name IN('Bruce', 'Luca', 'Taylor');
-- Bruce (367) 555-5533
-- Luca (389) 555-5198
-- Taylor (286) 555-6063


-- check for phone call for these numbers after 10.15 am on july 28 2021
select *
from phone_calls join people on phone_calls.caller = people.phone_number
where name IN('Talor', 'Bruce')
AND year = 2021
AND month = 7
AND day = 28
AND duration <60;
-- caller: Bruce
-- receiver: (375) 555-8161

select name
from people
where phone_number = '(375) 555-8161';