from bs4 import BeautifulSoup

html_content = """
<div id="faq-container"><h4 class="is-style-h4 has-charcoal-color mt-8"><b>Teaching Certification</b></h4>
                      <div class="new-accordion archive-faq-accordion"><details class="new-accordion-item" open="">
                <summary class="new-accordion-item__label archive-faq-label">
                Where can I find information about your accreditation and/or approval bodies?</summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="TextRun SCXW254688264 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW254688264 BCX0">You can find this information, including agency contact details, through the links provided on our </span></span><a class="Hyperlink SCXW254688264 BCX0" href="/about-moreland-university/" target="_blank" rel="noreferrer noopener"><span class="TextRun Underlined SCXW254688264 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="none"><span class="NormalTextRun SCXW254688264 BCX0">About Moreland University</span></span></a><span class="TextRun SCXW254688264 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW254688264 BCX0"> page or in </span><span class="NormalTextRun ContextualSpellingAndGrammarErrorV2Themed SCXW254688264 BCX0">our</span><span class="NormalTextRun SCXW254688264 BCX0"> </span></span><a class="Hyperlink SCXW254688264 BCX0" href="https://moreland.edu/wp-content/uploads/2023/08/Course-Catalog-Candidate-Handbook-23-24-Google-Docs.pdf%22" target="_blank" rel="noreferrer noopener"><span class="TextRun Underlined SCXW254688264 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="none"><span class="NormalTextRun SCXW254688264 BCX0">Course Catalog &amp; Candidate Handbook</span></span></a><span class="TextRun SCXW254688264 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW254688264 BCX0">. </span></span></p>
</div></details><details class="new-accordion-item" open="">
                <summary class="new-accordion-item__label archive-faq-label">
                How much does it cost?  </summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span data-contrast="auto">We offer affordable tuition for candidates seeking to complete our teacher preparation certification program or a Master’s in Education degree. </span><span data-ccp-props="{}">&nbsp;</span></p>
<p><span data-contrast="auto"> </span><span data-ccp-props="{}">&nbsp;</span></p>
<p><span data-contrast="auto">TEACH-NOW Teacher Preparation Certificate Program </span><span data-ccp-props="{}">&nbsp;</span></p>
<ul>
<li data-leveltext="" data-font="Symbol" data-listid="4" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Symbol&quot;,&quot;469769242&quot;:[8226],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="1" data-aria-level="1"><span data-ccp-props="{&quot;335559685&quot;:1080,&quot;335559731&quot;:0}">Full payment of $6,950 (As of April 30, 2024)</span></li>
<li data-leveltext="" data-font="Symbol" data-listid="4" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Symbol&quot;,&quot;469769242&quot;:[8226],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="2" data-aria-level="1"><span data-contrast="auto">Non-refundable registration fee of $200 included in this price </span><span data-ccp-props="{&quot;335559685&quot;:1080,&quot;335559731&quot;:0}">&nbsp;</span></li>
<li data-leveltext="" data-font="Symbol" data-listid="4" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Symbol&quot;,&quot;469769242&quot;:[8226],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="3" data-aria-level="1"><i><span data-contrast="auto">Payment Plan: </span></i><span data-contrast="auto"> </span><span data-ccp-props="{&quot;335559685&quot;:1080,&quot;335559731&quot;:0}">&nbsp;</span></li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li data-leveltext="o" data-font="Courier New" data-listid="5" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Courier New&quot;,&quot;469769242&quot;:[9675],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;o&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="1" data-aria-level="1"><span data-contrast="auto">Initial Payment – $950 USD </span><span data-ccp-props="{&quot;335559685&quot;:1800,&quot;335559731&quot;:0}">&nbsp;</span></li>
<li data-leveltext="o" data-font="Courier New" data-listid="5" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Courier New&quot;,&quot;469769242&quot;:[9675],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;o&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="2" data-aria-level="1"><span data-contrast="auto">Eight (8) Monthly Payments – $750 USD </span><span data-ccp-props="{&quot;335559685&quot;:1800,&quot;335559731&quot;:0}">&nbsp;</span></li>
</ul>
</li>
</ul>
<p><span data-contrast="auto"> </span><span data-ccp-props="{}">&nbsp;</span></p>
<p><span data-contrast="auto">Master’s in Education and Master’s in Educational Leadership Programs  </span><span data-ccp-props="{}">&nbsp;</span></p>
<ul>
<li data-leveltext="" data-font="Symbol" data-listid="6" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Symbol&quot;,&quot;469769242&quot;:[8226],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="1" data-aria-level="1"><span data-contrast="auto">Full payment of $14,000 (As of January 1, 2023) </span><span data-ccp-props="{&quot;335559685&quot;:1080,&quot;335559731&quot;:0}">&nbsp;</span></li>
<li data-leveltext="" data-font="Symbol" data-listid="6" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Symbol&quot;,&quot;469769242&quot;:[8226],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="2" data-aria-level="1"><span data-contrast="auto">Non-refundable registration fee of $200 included in this price </span><span data-ccp-props="{&quot;335559685&quot;:1080,&quot;335559731&quot;:0}">&nbsp;</span></li>
<li data-leveltext="" data-font="Symbol" data-listid="6" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Symbol&quot;,&quot;469769242&quot;:[8226],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="3" data-aria-level="1"><i><span data-contrast="auto">Payment Plan:</span></i><b><span data-contrast="auto"> </span></b><span data-contrast="auto"> </span><span data-ccp-props="{&quot;335559685&quot;:1080,&quot;335559731&quot;:0}">&nbsp;</span></li>
</ul>
<ul>
<li data-leveltext="o" data-font="Courier New" data-listid="7" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Courier New&quot;,&quot;469769242&quot;:[9675],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;o&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="1" data-aria-level="1"><span data-contrast="auto">Initial Payment  – $2,000 USD </span><span data-ccp-props="{&quot;335559685&quot;:1800,&quot;335559731&quot;:0}">&nbsp;</span></li>
<li data-leveltext="o" data-font="Courier New" data-listid="7" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Courier New&quot;,&quot;469769242&quot;:[9675],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;o&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="2" data-aria-level="1"><span data-contrast="auto">Twelve (12) Monthly Payments – $1,000 USD </span><span data-ccp-props="{&quot;335559685&quot;:1800,&quot;335559731&quot;:0}">&nbsp;</span></li>
</ul>
<p><span data-contrast="auto"> </span><span data-ccp-props="{}">&nbsp;</span></p>
<p><span data-contrast="auto">Master’s in Globalization and Education Research  </span><span data-ccp-props="{}">&nbsp;</span></p>
<ul>
<li data-leveltext="" data-font="Symbol" data-listid="8" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Symbol&quot;,&quot;469769242&quot;:[8226],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="4" data-aria-level="1"><span data-contrast="auto">Full payment of $14,500 (As of January 1, 2023) </span><span data-ccp-props="{&quot;335559685&quot;:1080,&quot;335559731&quot;:0}">&nbsp;</span></li>
<li data-leveltext="" data-font="Symbol" data-listid="8" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Symbol&quot;,&quot;469769242&quot;:[8226],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="5" data-aria-level="1"><span data-contrast="auto">Non-refundable registration fee of $200 included in this price </span><span data-ccp-props="{&quot;335559685&quot;:1080,&quot;335559731&quot;:0}">&nbsp;</span></li>
<li data-leveltext="" data-font="Symbol" data-listid="8" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Symbol&quot;,&quot;469769242&quot;:[8226],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="6" data-aria-level="1"><i><span data-contrast="auto">Payment Plan:</span></i><b><span data-contrast="auto"> </span></b><span data-contrast="auto"> </span><span data-ccp-props="{&quot;335559685&quot;:1080,&quot;335559731&quot;:0}">&nbsp;</span></li>
</ul>
<ul>
<li data-leveltext="o" data-font="Courier New" data-listid="9" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Courier New&quot;,&quot;469769242&quot;:[9675],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;o&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="3" data-aria-level="1"><span data-contrast="auto">Initial Payment  – $2,500 USD </span><span data-ccp-props="{&quot;335559685&quot;:1800,&quot;335559731&quot;:0}">&nbsp;</span></li>
<li data-leveltext="o" data-font="Courier New" data-listid="9" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Courier New&quot;,&quot;469769242&quot;:[9675],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;o&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="4" data-aria-level="1"><span data-contrast="auto">Twelve (12) Monthly Payments – $1,000 USD </span><span data-ccp-props="{&quot;335559685&quot;:1800,&quot;335559731&quot;:0}">&nbsp;</span></li>
</ul>
<ul>
<li data-leveltext="" data-font="Symbol" data-listid="10" data-list-defn-props="{&quot;335552541&quot;:1,&quot;335559684&quot;:-2,&quot;335559685&quot;:720,&quot;335559991&quot;:360,&quot;469769226&quot;:&quot;Symbol&quot;,&quot;469769242&quot;:[8226],&quot;469777803&quot;:&quot;left&quot;,&quot;469777804&quot;:&quot;&quot;,&quot;469777815&quot;:&quot;multilevel&quot;}" aria-setsize="-1" data-aria-posinset="7" data-aria-level="1"><span data-contrast="auto">Speak with an admissions representative to learn more about available payment plans. </span><span data-ccp-props="{&quot;335559685&quot;:1080,&quot;335559731&quot;:0}">&nbsp;</span></li>
</ul>
<p><span data-contrast="auto"><br>
</span><span data-ccp-props="{}">Sallie Mae also offers eligible Moreland University candidates loans with competitive interest rates and flexible repayment options — including deferred payments while in school and grace periods post-graduation. You can learn more about financing options with Sallie Mae® at moreland.edu/SallieMae </span></p>
<p><span data-ccp-props="{}"><a href="/request-info">Speak with an admissions representative to learn more about tuition payments or our partnership with Sallie Mae.</a></span></p>
<p><span data-contrast="auto">If your plans change after you start or you’re unhappy for any reason, please refer to our </span><a href="/refund-policy/"><span data-contrast="none">refund policy</span></a><span data-contrast="auto">. </span><span data-ccp-props="{}">&nbsp;</span></p>
</div></details><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                Do I have to pass any tests in order to get certified? </summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span data-contrast="auto">Yes, and it varies by state. It is important to determine what additional or specific requirements your state may have for certification. For example, some states require subject-specific exams or completing courses in a state’s history and culture. You can find out the requirements for the state you wish to get a license in by visiting the teaching licensing page of that state’s Department of Education or Professional Teaching Standards Board. Or, learn more about state certification through our TEACH-NOW program.   </span><span data-ccp-props="{}">&nbsp;</span></p>
<p><span data-contrast="auto"> </span><span data-contrast="auto">If you are seeking reciprocity in other states, you may need to take additional (or other) standardized tests. Speak with your program advisor if you have any additional questions about certification requirements. </span><span data-ccp-props="{}">&nbsp;</span></p>
<p><span data-contrast="auto"> </span><span data-ccp-props="{}">&nbsp;</span><span data-contrast="auto">We are here to help you determine specific requirements for your desired teaching location. </span><span data-ccp-props="{}">&nbsp;</span></p>
</div></details><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                After I complete the program, will I be able to teach in any state?  </summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span data-contrast="auto">Each state has its own requirements for granting teaching licenses (also called teaching certificates) through its Department of Education. You’ll be able to teach in the state where you are certified. Moreland will prepare candidates for certification in DC, WV, FL, GA, AZ. After a candidate completes the program, they may be able to pursue a teaching certificate through reciprocity but should ultimately consult with the State Department of Education for the state where they plan to move/seek certification to determine process and requirements. Note that state requirements change regularly, so stay connected to your Program Advisor and Certification Office at Moreland to assist you. You can find this information by searching the Department of Education for your desired state and searching for reciprocity guidelines. </span><span data-ccp-props="{}">&nbsp;</span></p>
<p><span data-contrast="auto"> </span><span data-ccp-props="{}">&nbsp;</span></p>
<p><span data-contrast="auto">Many international schools may recognize a certificate from a U.S. state. It is important to understand the requirements of where you plan to teach before pursuing certification.  </span><span data-ccp-props="{}">&nbsp;</span></p>
<p><span data-contrast="auto"> </span><span data-ccp-props="{}">&nbsp;</span></p>
<p><span data-contrast="auto">We are here to assist you throughout the licensure process.</span></p>
</div></details><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                Can I take this program while abroad?</summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="NormalTextRun SCXW31678304 BCX0">Moreland University has many current candidates and alumni living and working abroad. </span><span class="NormalTextRun AdvancedProofingIssueV2Themed SCXW31678304 BCX0">As long as</span><span class="NormalTextRun AdvancedProofingIssueV2Themed SCXW31678304 BCX0"> you have access to a computer with internet access and a webcam, you can complete our programs from anywhere in the world.</span><span class="NormalTextRun SCXW31678304 BCX0"> Even students without U.S. citizenship can complete the program and obtain a teaching license.</span></p>
</div></details><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                Can I REALLY learn how to teach from an online course?  </summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="TextRun SCXW199775487 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW199775487 BCX0">Yes, absolutely! In fact, in her 2019 Ph.D. dissertation at Boston College, Dr. Molly Cummings </span><span class="NormalTextRun ContextualSpellingAndGrammarErrorV2Themed SCXW199775487 BCX0">Carney,</span><span class="NormalTextRun SCXW199775487 BCX0"> completed a comprehensive review of Moreland University’s TEACH-NOW</span></span><span class="TextRun SCXW199775487 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW199775487 BCX0">®</span></span><span class="TextRun SCXW199775487 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW199775487 BCX0"> Teacher Preparation Certificate Program as a modern method of teacher preparation. Her results were clear that the TEACH-NOW program was dramatically more effective than traditional methods of preparation. You can read our summary of her work on our </span></span><a class="Hyperlink SCXW199775487 BCX0" href="/resources/blog-insights/preparing-teachers-for-tomorrow-dissertation-sm2ht/" target="_blank" rel="noreferrer noopener"><span class="TextRun Underlined SCXW199775487 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="none"><span class="NormalTextRun SCXW199775487 BCX0">blog</span></span></a><span class="TextRun SCXW199775487 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW199775487 BCX0">, with a link to the full dissertation. </span></span><span class="EOP SCXW199775487 BCX0" data-ccp-props="{}">&nbsp;</span></p>
</div></details><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                 Is this a real teaching certification? </summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span data-contrast="auto">Successful completion of our program leads to licensure exam eligibility, meaning that you can obtain a real teaching certificate, which is issued by a state department of education.  </span><span data-ccp-props="{}">&nbsp;</span></p>
<p><span data-contrast="auto"> </span><span data-contrast="auto">To be clear, only government entities have the legitimacy to grant a teaching certificate (license, qualification) directly. Every state reviews its own certification applications, according to its own requirements. </span><span data-ccp-props="{}">&nbsp;</span></p>
<p><span data-contrast="auto"> </span><span data-contrast="auto">Moreland University’s TEACH-NOW Teacher Preparation Certificate Program is a state-approved, accredited teacher preparation program in the District of Columbia (D.C.), Arizona, Florida, and West Virginia. Candidates who successfully complete our program are qualified to apply for a fully renewable teaching license (credential, certificate, qualification) from one of those states, provided they meet the applicable requirements of the state board of education.  </span><span data-ccp-props="{}">&nbsp;</span></p>
<p><span data-contrast="auto"> </span><span data-contrast="auto">Additionally, through reciprocity agreements, they may be eligible to obtain fully renewable teaching certificates or licenses from most other states, provided they meet the applicable licensing requirements of those states. </span><span data-ccp-props="{}">&nbsp;</span></p>
<p><span data-contrast="auto"> </span><span data-contrast="auto">In the United States, whoever desires a teaching credential (license, certificate, qualification) must first successfully complete an approved teacher preparation program in a given state, then apply directly to that state and meet all its requirements (normally including examinations), in order to be awarded the legitimate, recognized teaching credential. </span><span data-ccp-props="{}">&nbsp;</span></p>
</div></details></div><h4 class="is-style-h4 has-charcoal-color mt-8"><b>Program Modules</b></h4>
                      <div class="new-accordion archive-faq-accordion"><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                What is the purpose of the Program Orientation module? </summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="TextRun SCXW220545175 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW220545175 BCX0">The Program Orientation is your first step in the certification journey. </span><span class="NormalTextRun SCXW220545175 BCX0">It’s</span><span class="NormalTextRun SCXW220545175 BCX0"> designed to introduce you to your cohort and the online collaboration tools </span><span class="NormalTextRun SCXW220545175 BCX0">you’ll</span><span class="NormalTextRun SCXW220545175 BCX0"> be using. It will also prepare you for the overall structure and expectations of the program. </span></span><span class="EOP SCXW220545175 BCX0" data-ccp-props="{}">&nbsp;</span></p>
</div></details><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                How long does each module take to complete?</summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="TextRun SCXW152833975 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW152833975 BCX0">The duration for each module varies, but most of the modules are 4+ weeks. Some modules may require more time, such as the Teacher Practice &amp; Proficiency module, which spans </span><span class="NormalTextRun AdvancedProofingIssueV2Themed SCXW152833975 BCX0">12 weeks</span><span class="NormalTextRun SCXW152833975 BCX0">. </span></span><span class="EOP SCXW152833975 BCX0" data-ccp-props="{}">&nbsp;</span></p>
</div></details><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                Is there an order to complete the modules?</summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="NormalTextRun SCXW49077187 BCX0">Yes, the modules are designed to be sequential creating a comprehensive and connected learning experience, starting with the Program </span><span class="NormalTextRun SCXW49077187 BCX0">Orientation</span><span class="NormalTextRun SCXW49077187 BCX0"> and ending with Teacher Practice &amp; </span><span class="NormalTextRun SCXW49077187 BCX0">Proficiency</span><span class="NormalTextRun SCXW49077187 BCX0">.</span></p>
</div></details><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                What happens during the Teacher Practice &amp; Proficiency module?</summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="NormalTextRun SCXW182407619 BCX0">This is the 12-week clinical practice or student teaching part of the program where </span><span class="NormalTextRun SCXW182407619 BCX0">you’ll</span><span class="NormalTextRun SCXW182407619 BCX0"> work in a classroom alongside a mentor teacher. </span><span class="NormalTextRun SCXW182407619 BCX0">You’ll</span><span class="NormalTextRun SCXW182407619 BCX0"> engage in hands-on teaching and </span><span class="NormalTextRun SCXW182407619 BCX0">participate</span><span class="NormalTextRun SCXW182407619 BCX0"> in reflective and collaborative practices with your cohort.</span></p>
</div></details><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                Are there assessments or exams for each module?</summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="TextRun SCXW22743051 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW22743051 BCX0">Yes, assessments are integrated throughout the program to gauge your understanding and application of the material. Some modules have more formal assessments, such as the Student Assessments and Teacher Practice &amp; Proficiency modules.</span></span></p>
</div></details><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                What kind of support will I receive during the modules?</summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="NormalTextRun SCXW192472078 BCX0">Throughout the program, </span><span class="NormalTextRun SCXW192472078 BCX0">you’ll</span><span class="NormalTextRun SCXW192472078 BCX0"> have access to faculty, mentors, and program advisors who can offer guidance, feedback, and </span><span class="NormalTextRun SCXW192472078 BCX0">assistance</span><span class="NormalTextRun SCXW192472078 BCX0"> as needed.  </span><span class="NormalTextRun SCXW192472078 BCX0">You’ll</span><span class="NormalTextRun SCXW192472078 BCX0"> also find your classmates in your cohort will become a great network of support.</span></p>
</div></details><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                Can I work full-time while completing the program?</summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="NormalTextRun SCXW116444604 BCX0">Many of our students work while enrolled. Keep in mind that the Teacher Practice &amp; Proficiency module requires </span><span class="NormalTextRun SCXW116444604 BCX0">a significant time</span><span class="NormalTextRun SCXW116444604 BCX0"> commitment and may interfere with a full-time work schedule if you are not already a full-time teacher or working full-time in a school.</span></p>
</div></details><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                What if I have more questions about a specific module?</summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="TextRun SCXW255079843 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW255079843 BCX0">Speak with your faculty member or contact your program advisor. You can also refer to the detailed descriptions</span></span><span class="TextRun SCXW255079843 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"> <span class="NormalTextRun SCXW255079843 BCX0">provided for</span><span class="NormalTextRun SCXW255079843 BCX0"> each module. </span><span class="NormalTextRun SCXW255079843 BCX0">We’re</span><span class="NormalTextRun SCXW255079843 BCX0"> here to ensure you have all the information you need to succeed.</span></span></p>
</div></details></div><h4 class="is-style-h4 has-charcoal-color mt-8"><b>General</b></h4>
                      <div class="new-accordion archive-faq-accordion"><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                Do you have a Course Catalog &amp; Candidate Handbook for review? </summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="TextRun SCXW205423737 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW205423737 BCX0">Yes. You can access a copy of the </span></span><a class="Hyperlink SCXW205423737 BCX0" href="https://moreland.edu/wp-content/uploads/2024/05/Candidate-Handbook_2023_2024_May2024.pdf" target="_blank" rel="noreferrer noopener"><span class="TextRun Underlined SCXW205423737 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="none"><span class="NormalTextRun SCXW205423737 BCX0">handbook</span></span></a><span class="TextRun SCXW205423737 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW205423737 BCX0"> here. Our Admissions Team is here to review our </span><span class="NormalTextRun ContextualSpellingAndGrammarErrorV2Themed SCXW205423737 BCX0">offerings</span><span class="NormalTextRun SCXW205423737 BCX0"> and answer your questions. </span></span><span class="EOP SCXW205423737 BCX0" data-ccp-props="{}">&nbsp;</span></p>
</div></details><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                What are the technology requirements for effective participation?</summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="TextRun SCXW194000075 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW194000075 BCX0">To </span><span class="NormalTextRun SCXW194000075 BCX0">participate</span><span class="NormalTextRun SCXW194000075 BCX0"> effectively in our online programs, you will require a high-speed internet connection (more than 10 Mbps download at </span></span><a class="Hyperlink SCXW194000075 BCX0" href="http://speedtest.net/" target="_blank" rel="noreferrer noopener"><span class="TextRun Underlined SCXW194000075 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="none"><span class="NormalTextRun SCXW194000075 BCX0">speedtest.net</span></span></a><span class="TextRun SCXW194000075 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW194000075 BCX0">); a webcam; a microphone; and a headset or speakers. </span></span><span class="EOP SCXW194000075 BCX0" data-ccp-props="{}">&nbsp;</span></p>
</div></details></div><h4 class="is-style-h4 has-charcoal-color mt-8"><b>Admissions</b></h4>
                      <div class="new-accordion archive-faq-accordion"><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                I don’t have a minimum GPA of 3.0. What are my options?</summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="TextRun SCXW154126043 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW154126043 BCX0">In lieu of a 3.0 undergraduate GPA, under our Exceptions Policy, applicants may qualify for acceptance through proven work experience. Please </span></span><a class="Hyperlink SCXW154126043 BCX0" href="https://moreland.edu/request-info/" target="_blank" rel="noreferrer noopener"><span class="TextRun Underlined SCXW154126043 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="none"><span class="NormalTextRun SCXW154126043 BCX0">contact us</span></span></a><span class="TextRun SCXW154126043 BCX0" lang="EN-US" xml:lang="EN-US" data-contrast="auto"><span class="NormalTextRun SCXW154126043 BCX0"> for any further questions or clarifications. </span></span></p>
</div></details></div><h4 class="is-style-h4 has-charcoal-color mt-8"><b>Masters</b></h4>
                      <div class="new-accordion archive-faq-accordion"><details class="new-accordion-item">
                <summary class="new-accordion-item__label archive-faq-label">
                Can I earn a certification through a Master's program?</summary>
                <div class="new-accordion-item__content archive-faq-content">
                <p><span class="NormalTextRun SCXW68382248 BCX0">Our master’s in education degrees in six areas of specialization include the certification preparation coursework, earning you the credentials you need to apply for state certification. In </span><span class="NormalTextRun ContextualSpellingAndGrammarErrorV2Themed SCXW68382248 BCX0">additional</span><span class="NormalTextRun SCXW68382248 BCX0"> the certification preparation coursework, you will need to submit additional materials to apply for certification. These can often include exams, </span><span class="NormalTextRun SCXW68382248 BCX0">additional</span><span class="NormalTextRun SCXW68382248 BCX0"> training, </span><span class="NormalTextRun SCXW68382248 BCX0">fingerprints</span><span class="NormalTextRun SCXW68382248 BCX0"> and a background check. Learn more about state certification requirements by exploring the states we support here</span><span class="NormalTextRun SCXW68382248 BCX0">.</span></p>
</div></details></div></div>
"""


# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all details elements
details_elements = soup.find_all('details', class_='new-accordion-item')

# Iterate through each details element
for details_element in details_elements:
    # Find the summary tag
    summary_tag = details_element.find('summary', class_='new-accordion-item__label archive-faq-label')

    # Extract the text within the summary tag
    if summary_tag:
        result_summary = summary_tag.get_text(strip=True)
        print("Summary:", result_summary)

    # Find the div tag containing the content
    content_div = details_element.find('div', class_='new-accordion-item__content archive-faq-content')

    # Extract the text within the content div
    if content_div:
        result_content = content_div.get_text(strip=True)
        print("Content:", result_content)

    print()  # Add a newline between each details element