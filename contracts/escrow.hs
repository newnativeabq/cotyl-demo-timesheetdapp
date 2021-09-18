{-# LANGUAGE OverloadedStrings #-}
module Example where

import           Language.Marlowe.Extended

main :: IO ()
main = print . pretty $ contract


{- Define a contract, Close is the simplest contract which just ends the contract straight away
-}

contract :: Contract
contract = 
    When
        [Case
            (Deposit
                (Role "employer")
                (Role "employer")
                (Token "" "")
                (ConstantParam "contractAmount")
            )
            (When
                [Case
                    (Choice
                        (ChoiceId
                            "validateAmt"
                            (Role "employee")
                        )
                        [Bound 0 1]
                    )
                    (If
                        (ValueEQ
                            (ChoiceValue
                                (ChoiceId
                                    "validateAmt"
                                    (Role "employee")
                                ))
                            (Constant 1)
                        )
                        (When
                            [Case
                                (Choice
                                    (ChoiceId
                                        "approve"
                                        (Role "employer")
                                    )
                                    [Bound 0 1]
                                )
                                (If
                                    (ValueEQ
                                        (ChoiceValue
                                            (ChoiceId
                                                "approve"
                                                (Role "employer")
                                            ))
                                        (Constant 1)
                                    )
                                    (Pay
                                        (Role "employer")
                                        (Account (Role "employee"))
                                        (Token "" "")
                                        (ConstantParam "contractAmount")
                                        Close 
                                    )
                                    Close 
                                )]
                            15 Close 
                        )
                        Close 
                    )]
                10 Close 
            )]
        5 Close 
