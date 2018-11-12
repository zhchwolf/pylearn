/*
   Microsoft SQL Server Integration Services Script Task
   Write scripts using Microsoft Visual C# 2008.
   The ScriptMain is the entry point class of the script.
*/

using System;
using System.Data;
using System.Data.SqlClient;
using Microsoft.SqlServer.Dts.Runtime;
using System.Windows.Forms;

namespace ST_a0106bf9db35453b9f7799d165cdd786.csproj
{
    [System.AddIn.AddIn("ScriptMain", Version = "1.0", Publisher = "", Description = "")]
    public partial class ScriptMain : Microsoft.SqlServer.Dts.Tasks.ScriptTask.VSTARTScriptObjectModelBase
    {

        #region VSTA generated code
        enum ScriptResults
        {
            Success = Microsoft.SqlServer.Dts.Runtime.DTSExecResult.Success,
            Failure = Microsoft.SqlServer.Dts.Runtime.DTSExecResult.Failure
        };
        #endregion

        /*
		The execution engine calls this method when the task executes.
		To access the object model, use the Dts property. Connections, variables, events,
		and logging features are available as members of the Dts property as shown in the following examples.

		To reference a variable, call Dts.Variables["MyCaseSensitiveVariableName"].Value;
		To post a log entry, call Dts.Log("This is my log text", 999, null);
		To fire an event, call Dts.Events.FireInformation(99, "test", "hit the help message", "", 0, true);

		To use the connections collection use something like the following:
		ConnectionManager cm = Dts.Connections.Add("OLEDB");
		cm.ConnectionString = "Data Source=localhost;Initial Catalog=AdventureWorks;Provider=SQLNCLI10;Integrated Security=SSPI;Auto Translate=False;";

		Before returning from this method, set the value of Dts.TaskResult to indicate success or failure.
		
		To open Help, press F1.
	*/

        public void Main()
        {
            //参数：User::vHCA,User::vHCP,User::vProd
            var vHCACode = Dts.Variables["vHCA"].ToString();
            var vHCPCode = Dts.Variables["vHCP"].ToString();
            var vProdCode = Dts.Variables["vProd"].ToString();

            //返回值：User::vString
            var vString = Dts.Variables["vString"].ToString();

            //TODO - 添加数据库连接字符串
            var conString = @"TODO - 添加数据库连接字符串";
            SqlConnection sqlConnection = new SqlConnection(conString);
            SqlCommand sqlCommond = new SqlCommand();
            SqlDataAdapter sqlDataAdapter = new SqlDataAdapter();
            sqlConnection.Open();

            string commondText = @"";
            sqlCommond.CommandText = commondText;
            sqlCommond.Parameters.Add("@HCACode", SqlDbType.NVarChar, 50);      //医院Code
            sqlCommond.Parameters.Add("@HCPCode", SqlDbType.NVarChar, 50);      //客户Code
            sqlCommond.Parameters.Add("@ProdCode", SqlDbType.NVarChar, 50);     //产品Code

            sqlCommond.Parameters.Add("@PSPeriodId", SqlDbType.Int);   //产品周期ID
            sqlCommond.Parameters.Add("@PQstnaireId", SqlDbType.NVarChar, 50);  //产品问卷ID
            sqlCommond.Parameters.Add("@QstnaireId", SqlDbType.NVarChar, 50);   //问卷ID

            sqlCommond.Parameters["@HCACode"].Value = vHCACode;
            sqlCommond.Parameters["@HCPCode"].Value = vHCPCode;
            sqlCommond.Parameters["@ProdCode"].Value = vProdCode;
            sqlCommond.Parameters["@PSPeriodId"].Value = string.Empty;
            sqlCommond.Parameters["@PQstnaireId"].Value = string.Empty;
            sqlCommond.Parameters["@QstnaireId"].Value = string.Empty;

            #region 获取客户基本信息

            commondText = @"select * from HCP where HCPCode = @HCPCode and HCPStatus = 1 ";
            sqlCommond.CommandText = commondText;
            sqlDataAdapter = new SqlDataAdapter(sqlCommond);

            DataTable dtHcp = new DataTable();
            sqlDataAdapter.Fill(dtHcp);
            if (dtHcp.Rows.Count != 1)
            {
                vString = dtHcp.Rows.Count == 0 ? "数据获取异常：客户基本信息不存在." : "数据获取异常：存在多条客户基本信息.";
                Dts.TaskResult = (int)ScriptResults.Failure;
                goto MainEnd;
            }

            #endregion

            #region 获取问卷信息

            commondText = @"select prod_period.ProductSurveyPeriodID, ProductQuestionnaire.ProductQuestionnaireID, prod_qnaire.IsCoreOrEmerging,Questionnaire.* from 
                                (select * from InstProd where HCACode = @HCACode and ProductCode = @ProdCode and YM = CONVERT(varchar(6),GETDATE(),112) and ActiveStatus = 1 ) inst_prod
                                inner join 
                                (select * from ProductSurveyPeriod where ProductCode = @ProdCode and PeriodStartDate <= GETDATE() and PeriodEndDate >= GETDATE() and ActiveStatus = 1) prod_period
                                on inst_prod.ProductCode = prod_period.ProductCode
                                inner join 
                                (select * from ProductQuestionnaire where ProductCode = @ProdCode and ActiveStatus = 1) prod_qnaire
                                on inst_prod.IsCoreOrEmerging = prod_qnaire.IsCoreOrEmerging
                                inner join Questionnaire on prod_qnaire.QuestionnaireID = Questionnaire.QuestionnaireID";
            sqlCommond.CommandText = commondText;
            sqlDataAdapter = new SqlDataAdapter(sqlCommond);

            DataTable dtQuestionnaire = new DataTable();
            sqlDataAdapter.Fill(dtQuestionnaire);
            if (dtQuestionnaire.Rows.Count != 1)
            {
                vString = dtQuestionnaire.Rows.Count == 0 ? "数据获取异常：问卷信息不存在." : "数据获取异常：存在多条问卷信息.";
                Dts.TaskResult = (int)ScriptResults.Failure;
                goto MainEnd;
            }

            #endregion

            #region 获取问题信息

            string productSurveyPeriodId = dtQuestionnaire.Rows[0]["ProductSurveyPeriodID"].ToString();
            string productQuestionnaireID = dtQuestionnaire.Rows[0]["ProductQuestionnaireID"].ToString();
            string questionnaireId = dtQuestionnaire.Rows[0]["QuestionnaireID"].ToString();
            sqlCommond.Parameters["@PSPeriodId"].Value = productSurveyPeriodId;
            sqlCommond.Parameters["@PQstnaireId"].Value = productQuestionnaireID;
            sqlCommond.Parameters["@QstnaireId"].Value = questionnaireId;
            commondText = @"select * from Question where QuestionnaireID = @QstnaireId and QuestionEnable = 1";
            sqlCommond.CommandText = commondText;
            sqlDataAdapter = new SqlDataAdapter(sqlCommond);

            DataTable dtQuestion = new DataTable();
            sqlDataAdapter.Fill(dtQuestion);
            if (dtQuestion.Rows.Count < 0)
            {
                vString = "数据获取异常：问题信息不存在.";
                Dts.TaskResult = (int)ScriptResults.Failure;
                goto MainEnd;

            }
            
            #endregion

            #region 获取潜力主数据信息

            commondText = @"select * from InstDoc where ParentCustomerCode = @HCACode and ChildCustomerCode = @HCPCode and ActiveStatus = 1"; 
            sqlCommond.CommandText = commondText;
            sqlDataAdapter = new SqlDataAdapter(sqlCommond);

            DataTable dtInstDoc = new DataTable ();
            sqlDataAdapter.Fill(dtInstDoc);
            if (dtInstDoc.Rows.Count == 0)
            {
                vString = "数据获取异常：潜力主数据信息不存在.";
                Dts.TaskResult = (int)ScriptResults.Failure;
                goto MainEnd;
            }

            #endregion

            #region 获取答案信息

            commondText = @"select ProductSurveyResult.* from 
                                HCP inner join ProductSurveyResult
                                on HCP.HCPID = ProductSurveyResult.HCPID
                                and HCP.HCPCode = @HCPCode
                                and ProductSurveyResult.ProductCode = @ProdCode
                                and ProductSurveyResult.ProductSurveyPeriodID = @PSPeriodId
                                and HCP.HCPStatus = 1
                                and ProductSurveyResult.SurveyStatus = 1";
            sqlCommond.CommandText = commondText;
            sqlDataAdapter = new SqlDataAdapter(sqlCommond);

            DataTable dtSurveyResult = new DataTable();
            sqlDataAdapter.Fill(dtSurveyResult);
            if (dtSurveyResult.Rows.Count > dtQuestion.Rows.Count)
            {
                vString = "数据获取异常：答案信息多于问题信息.";
                Dts.TaskResult = (int)ScriptResults.Failure;
                goto MainEnd;
            }

            #endregion

            #region 获取公式和等级区间

            string countformula = dtQuestionnaire.Rows[0]["CountFormula"].ToString();
            string[] sGradevalue = dtQuestionnaire.Rows[0]["GradeValue"].ToString().Split(new char[] { '#' });
            string[] sGradescorelowerlimit = dtQuestionnaire.Rows[0]["GradeScoreLowerLimit"].ToString().Split(new char[] { '#' });
            string[] sGradescoreupperlimit = dtQuestionnaire.Rows[0]["GradeScoreUpperLimit"].ToString().Split(new char[] { '#' });
            string[] sGradetargeting = dtQuestionnaire.Rows[0]["GradeTargeting"].ToString().Split(new char[] { '#' });

            #endregion

            #region 计算公式,获取 potentialValue

            for (int index = 0; index < dtQuestion.Rows.Count; index++)
            {
                if (countformula.IndexOf("[ " + (index + 1).ToString() + " ]") == -1)
                {
                    continue;
                }
                var replaceValue = string.Empty;

                #region 获取 replaceValue

                foreach (DataRow drSurveyResult in dtSurveyResult.Rows)
                {
                    if (drSurveyResult["QuestionID"] == dtQuestion.Rows[index]["QuestionID"].ToString())
                    {
                        string answercontent = string.Empty;
                        string answerscore = string.Empty;
                        string answerweight = string.Empty;

                        switch (Convert.ToInt32(dtQuestion.Rows[index]["QuestionType"]))
                        {
                            case 1://填空题
                                answercontent = !string.IsNullOrEmpty(drSurveyResult["AnswerContent"].ToString()) ? Convert.ToDecimal(drSurveyResult["AnswerContent"].ToString()).ToString("f5") : "0.0";
                                replaceValue = Convert.ToDecimal(answercontent).ToString("f5");
                                break;
                            case 2://下拉选择
                            case 3://单选题
                                answerscore = !string.IsNullOrEmpty(drSurveyResult["AnswerScore"].ToString()) ? Convert.ToDecimal(drSurveyResult["AnswerScore"].ToString()).ToString("f5") : "0.0";
                                answerweight = !string.IsNullOrEmpty(drSurveyResult["AnswerWeight"].ToString()) ? Convert.ToDecimal(drSurveyResult["AnswerWeight"].ToString()).ToString("f5") : "0.0";
                                replaceValue = Convert.ToDecimal(Convert.ToDecimal(answerscore) * Convert.ToDecimal(answerweight) * Convert.ToDecimal("0.01")).ToString("f5");
                                break;
                            case 5://主数据
                                var maindataResult = string.Empty;
                                var mdmaptable = dtQuestion.Rows[index]["MDMapTable"].ToString();   //主数据只 Map HCP 基本信息
                                var mdmapcolumn = dtQuestion.Rows[index]["MDMapColumn"].ToString(); //HCP 基本信息 属性值

                                //Edit By Marvin.Ma 2013-08-28
                                #region 获取 replaceValue 值

                                switch (mdmaptable.ToUpper())
                                {
                                    case "HCP":
                                        switch (mdmapcolumn.ToUpper())
                                        {
                                            #region 获取 主数据问题 结果

                                            case "LANGUAGE": //语言
                                                maindataResult = dtHcp.Rows[0]["HCPLanguage"].ToString();
                                                break;
                                            case "HOBBY": //兴趣爱好
                                                maindataResult = dtHcp.Rows[0]["HCPHobby"].ToString();
                                                break;
                                            case "HCPFLAG": //Hcp 标志
                                                maindataResult = dtHcp.Rows[0]["HCPFlag"].ToString();
                                                break;
                                            case "HCPTYPE": //客户类型
                                                maindataResult = dtHcp.Rows[0]["HCPType"].ToString();
                                                break;
                                            case "DEPARTMENT": //部门
                                                maindataResult = dtHcp.Rows[0]["Department"].ToString();
                                                break;
                                            case "LABORATORY": //科室
                                                maindataResult = dtHcp.Rows[0]["Laboratory"].ToString();
                                                break;
                                            case "TITLE": //职称
                                                maindataResult = dtHcp.Rows[0]["Title"].ToString();
                                                break;
                                            case "QUALIFICATION": //资历
                                                maindataResult = dtHcp.Rows[0]["TitleQualification"].ToString();
                                                break;
                                            case "ADMINISTRATIVEPOST": //行政职务
                                                maindataResult = dtHcp.Rows[0]["AdministrativePost"].ToString();
                                                break;
                                            case "SPECIALITY": //专业领域
                                                maindataResult = dtHcp.Rows[0]["Speciality"].ToString();
                                                break;
                                            default:
                                                break;

                                            #endregion
                                        }

                                        string[] answerTextList = dtQuestion.Rows[index]["AnswerText"].ToString().Split('#');
                                        for (int iAnswerText = 0; iAnswerText < answerTextList.Length; iAnswerText++)
                                        {
                                            if (answerTextList[iAnswerText] == maindataResult)
                                            {
                                                answerscore = !string.IsNullOrEmpty(dtQuestion.Rows[index]["AnswerScore"].ToString())
                                                                ? dtQuestion.Rows[index]["AnswerScore"].ToString().Split('#')[iAnswerText]
                                                                : string.Empty;
                                                answerweight = !string.IsNullOrEmpty(dtQuestion.Rows[index]["AnswerWeight"].ToString())
                                                                ? dtQuestion.Rows[index]["AnswerWeight"].ToString().Split('#')[iAnswerText]
                                                                : string.Empty;
                                                break;
                                            }
                                        }
                                        answerscore = !string.IsNullOrEmpty(answerscore) ? Convert.ToDecimal(answerscore).ToString("f5") : "1.0";
                                        answerweight = !string.IsNullOrEmpty(answerweight) ? Convert.ToDecimal(answerweight).ToString("f5") : "100.0";
                                        replaceValue = Convert.ToDecimal(Convert.ToDecimal(answerscore) * Convert.ToDecimal(answerweight) * Convert.ToDecimal("0.01")).ToString("f5");
                                        break;
                                    case "INSTDOC":
                                        switch (mdmapcolumn.ToUpper())
                                        {
                                            #region 获取 潜力主数据问题 结果

                                            case "WORKDAYSCODE":    //每周门诊半天数
                                                maindataResult = !string.IsNullOrEmpty(dtInstDoc.Rows[0]["WorkdaysCode"].ToString()) != null ? Convert.ToDecimal(dtInstDoc.Rows[0]["WorkdaysCode"].ToString()).ToString("f5") : "0.00000";
                                                break;
                                            case "PATIENTNUM":      //每半天门诊病人数
                                                maindataResult = !string.IsNullOrEmpty(dtInstDoc.Rows[0]["PatientNum"].ToString()) != null ? Convert.ToDecimal(dtInstDoc.Rows[0]["PatientNum"].ToString()).ToString("f5") : "0.00000"; 
                                                break;
                                            case "BEDNUM":          //负责病床数
                                                maindataResult = !string.IsNullOrEmpty(dtInstDoc.Rows[0]["BedNum"].ToString()) != null ? Convert.ToDecimal(dtInstDoc.Rows[0]["BedNum"].ToString()).ToString("f5") : "0.00000"; 
                                                break;
                                            case "HOSPITALIZEDDAYS"://平均住院天数
                                                maindataResult = string.IsNullOrEmpty(dtInstDoc.Rows[0]["HospitalizedDays"].ToString()) != null ? Convert.ToDecimal(dtInstDoc.Rows[0]["HospitalizedDays"].ToString()).ToString("f5") : "0.00000"; 
                                                break;
                                            default:
                                                break;

                                            #endregion
                                        }
                                        replaceValue = Convert.ToDecimal(maindataResult).ToString("f5");
                                        break;
                                }

                                #endregion
                                break;
                            case 4://日期
                            case 6://标签
                                break;
                            default:
                                break;
                        }
                        break;
                    }
                }

                #endregion

                countformula = countformula.Replace("[ " + (index + 1).ToString() + " ]", replaceValue);
            }

            sqlCommond.CommandText = countformula;
            countformula = Convert.ToDecimal(sqlCommond.ExecuteScalar()).ToString("f5");
            decimal potentialValue = Convert.ToDecimal(countformula);
            for (int i = 0; i < sGradevalue.Length; i++)
            {
                if (Convert.ToDecimal(sGradescorelowerlimit[i].ToString()) <= potentialValue && Convert.ToDecimal(sGradescoreupperlimit[i].ToString()) > potentialValue)
                {
                    vString = string.Format("{0}#{1}#{2}",sGradevalue[i].ToString(),(int?)Convert.ToDecimal(sGradetargeting[i].Trim()),Convert.ToDecimal(countformula));
                    break;
                }
            }

            Dts.TaskResult = (int)ScriptResults.Success;
            goto MainEnd;

            #endregion


        MainEnd:
            sqlDataAdapter.Dispose();
            sqlCommond.Dispose();
            sqlConnection.Close();
            sqlConnection.Dispose();
        }

    }
}