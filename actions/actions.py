from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import spacy

nlp = spacy.load("en_core_web_md")
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Load the spaCy model


class ActionExplainInvestopedia(Action):

    def name(self) -> str:
        return "action_explain_investopedia"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        # Example of using spaCy for Named Entity Recognition
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        
        response = f"Investopedia is a comprehensive investment platform. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionExplainInvestopediaForEntrepreneurs(Action):

    def name(self) -> str:
        return "action_explain_investopedia_for_entrepreneurs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia provides a platform for entrepreneurs to connect with investors. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionRoleOfIncubators(Action):

    def name(self) -> str:
        return "action_role_of_incubators"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Incubators play a crucial role in helping startups grow by providing resources and mentorship. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

# Similarly, update the remaining action classes to include spaCy processing

class ActionHowToGetStarted(Action):

    def name(self) -> str:
        return "action_how_to_get_started"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"To get started with Investopedia, you need to create an account and complete the necessary KYC formalities. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionAccessFromMobile(Action):

    def name(self) -> str:
        return "action_access_from_mobile"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Yes, Investopedia can be accessed from mobile devices. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

# Continue updating all other actions similarly

class ActionPlatformSecurity(Action):

    def name(self) -> str:
        return "action_platform_security"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia uses advanced security measures to protect user data. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionBusinessTypes(Action):

    def name(self) -> str:
        return "action_business_types"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia supports various types of businesses including startups and established companies. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

# ... (continue updating the remaining actions in a similar fashion)

# Example of continuing the pattern for other actions
class ActionPivotBusiness(Action):

    def name(self) -> str:
        return "action_pivot_business"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia helps businesses pivot by providing them with new opportunities and resources. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionTeamDetails(Action):

    def name(self) -> str:
        return "action_team_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"You can find information about our team on the Investopedia website. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionContactSupport(Action):

    def name(self) -> str:
        return "action_contact_support"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"You can contact Investopedia support through email or phone. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

# Continue with the remaining actions...
class ActionKycApprovalTime(Action):

    def name(self) -> str:
        return "action_kyc_approval_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"KYC approval time typically takes a few days. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionProposalVerificationTime(Action):

    def name(self) -> str:
        return "action_proposal_verification_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Proposal verification time depends on the complexity of the proposal. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionEquityTransferProcess(Action):

    def name(self) -> str:
        return "action_equity_transfer_process"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"The equity transfer process is facilitated by legal documentation and verification. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionKittaAndPercent(Action):

    def name(self) -> str:
        return "action_kitta_and_percent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"A Kitta represents a share unit, and its percentage value depends on the total shares. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionPlatformFee(Action):

    def name(self) -> str:
        return "action_platform_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia charges a platform fee for using its services. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionMultipleInvestorsSameBid(Action):

    def name(self) -> str:
        return "action_multiple_investors_same_bid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"When multiple investors place the same bid, the allocation is usually based on a first-come, first-served basis. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionLocation(Action):

    def name(self) -> str:
        return "action_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia operates globally, with specific services available based on location. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionPlatformInvestment(Action):

    def name(self) -> str:
        return "action_platform_investment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia provides a platform for various investment opportunities. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionAccountCreationFee(Action):

    def name(self) -> str:
        return "action_account_creation_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia charges a small fee for account creation to cover administrative costs. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionInvestorEarlyExit(Action):

    def name(self) -> str:
        return "action_investor_early_exit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Early exit options for investors depend on the terms agreed upon with the entrepreneur. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionLegalDocuments(Action):

    def name(self) -> str:
        return "action_legal_documents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Legal documents required for investment are managed through the Investopedia platform. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionInvestorTypes(Action):

    def name(self) -> str:
        return "action_investor_types"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia supports various types of investors, including angel investors, venture capitalists, and more. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionManageFinancialTransactions(Action):

    def name(self) -> str:
        return "action_manage_financial_transactions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia provides tools to manage financial transactions securely. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionPaymentMethods(Action):

    def name(self) -> str:
        return "action_payment_methods"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia supports various payment methods, including bank transfers and online payments. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionPlatformFeeStructure(Action):

    def name(self) -> str:
        return "action_platform_fee_structure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"The platform fee structure is transparent and depends on the services used. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionStudentBenefits(Action):

    def name(self) -> str:
        return "action_student_benefits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Students can benefit from Investopedia by gaining access to educational resources and funding opportunities. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionPlatformSupportBusinessGrowth(Action):

    def name(self) -> str:
        return "action_platform_support_business_growth"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia supports business growth by connecting entrepreneurs with investors and providing strategic advice. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionEntrepreneurSupport(Action):

    def name(self) -> str:
        return "action_entrepreneur_support"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia offers support to entrepreneurs through mentorship and networking opportunities. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionTechnologyUsed(Action):

    def name(self) -> str:
        return "action_technology_used"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia uses advanced technology to ensure security and efficiency. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionTransactionFees(Action):

    def name(self) -> str:
        return "action_transaction_fees"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Transaction fees on Investopedia depend on the type and size of the transaction. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionKycImportance(Action):

    def name(self) -> str:
        return "action_kyc_importance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"KYC is important for verifying investor identity and compliance with regulations. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionBidWithdrawal(Action):

    def name(self) -> str:
        return "action_bid_withdrawal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investors can withdraw their bid before it is accepted by the entrepreneur. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionTeamChange(Action):

    def name(self) -> str:
        return "action_team_change"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Changes in the team are communicated through updates on the Investopedia platform. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionPlatformReputation(Action):

    def name(self) -> str:
        return "action_platform_reputation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Investopedia has built a strong reputation for facilitating successful investment opportunities. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []

class ActionSubmitProposal(Action):

    def name(self) -> str:
        return "action_submit_proposal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        last_message = tracker.latest_message.get('text')
        doc = nlp(last_message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = f"Entrepreneurs can submit their proposals through the Investopedia platform. Detected entities: {entities}"
        dispatcher.utter_message(text=response)
        return []